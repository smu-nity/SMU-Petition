from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.utils import timezone
from django.utils.datetime_safe import datetime

from accounts.models import Statistics2
from config.settings import CSRF_TRUSTED_ORIGINS, SUCCESS_VALUE
from petitions.decorators import superuser_required
from qna.forms import QnAForm, AnswerForm
from django.contrib import messages

from qna.models import qna, QnA_Answer


# Create your views here.
def home(request):
    return render(request, 'qna/QnA_list.html')


def QnA_list(request):
    sort_dic = {'0': '-create_date', '1': 'create_date'}
    pl = qna.objects
    sort = request.GET.get('sort', '0')
    page = request.GET.get('page', '1')
    pl = pl.order_by(sort_dic[sort])
    paginator = Paginator(pl, 5)
    page_obj = paginator.get_page(page)
    response = render(request, 'qna/QnA_list.html', {'QnA_list': page_obj, 'page': '모든 QnA'})
    if request.COOKIES.get('is_visit') is None:
        response.set_cookie('is_visit', 'visited', 60 * 30)
        st, _ = Statistics2.objects.get_or_create(date=datetime.date.today())
        st.visit_count += 1
        st.save()
    return response


def QnA_detail(request, QnA_id):
    QnA = get_object_or_404(qna, pk=QnA_id)
    url = f'{CSRF_TRUSTED_ORIGINS[0]}/qna/{QnA.pk}/'
    context = {'qna': QnA, 'url': url}
    answers = QnA_Answer.objects.filter(qna=QnA)
    if answers:
        context['answer'] = answers.first()
    response = render(request, 'qna/QnA_detail.html', context)
    if request.COOKIES.get('is_visit') is None:
        response.set_cookie('is_visit', 'visited', 60 * 30)
        st, _ = Statistics2.objects.get_or_create(date=datetime.date.today())
        st.visit_count += 1
        st.save()
    return response


# @login_required
def QnA_create(request):
    if request.method == 'POST':
        form = QnAForm(request.POST)
        if form.is_valid():
            QnA = form.save(commit=False)
            QnA.author = request.user
            QnA.save()
            return redirect('qna:QnA_list', 'progress')
    else:
        form = QnAForm()
    context = {'form': form}
    return render(request, 'qna/QnA_form.html', context)


# @login_required
def QnA_modify(request, QnA_id):
    QnA = get_object_or_404(qna, pk=QnA_id)
    if request.user != QnA.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('qna:QnA_detail', QnA_id=QnA.id)
    if request.method == "POST":
        form = QnAForm(request.POST, instance=QnA)
        if form.is_valid():
            QnA = form.save(commit=False)
            QnA.modify_date = timezone.now()  # 수정일시 저장
            QnA.save()
            return redirect('qna:QnA_detail', QnA_id=QnA.id)
    else:
        form = QnAForm(instance=QnA)
    context = {'form': form}
    return render(request, 'qna/QnA_form.html', context)


# @login_required
def QnA_delete(request, QnA_id):
    QnA = get_object_or_404(qna, pk=QnA_id)
    if request.user != QnA.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('qna:QnA_detail', qna_id=QnA.id)
    QnA.delete()
    return redirect('qna:QnA_detail', 'progress')


@superuser_required
def QnA_answer_create(request, QnA_id, type=None):
    QnA = get_object_or_404(qna, pk=QnA_id)
    if QnA_Answer.objects.filter(qna=QnA):
        messages.error(request, '이미 답변한 질문입니다.')
        return redirect('qna:QnA_detail', qna_id=QnA.id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.qna = QnA
            answer.save()
            QnA.end_date = datetime.datetime.now()
            QnA.save()
            return redirect('qna:QnA_detail', qna_id=QnA.id)
    else:
        form = AnswerForm()
    content = '답변 등록'
    if type == 'reject':
        content = '반려 이유'
    return render(request, 'qna/form.html', {'form': form, 'content': content, 'qna_id': QnA_id})


@superuser_required
def QnA_answer_modify(request, answer_id):
    answer = get_object_or_404(QnA_Answer, pk=answer_id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('qna:QnA_detail', qna_id=answer.qna.id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'qna/form.html', {'form': form, 'content': '답변 등록', 'qna_id': answer.qna.id})


@superuser_required
def QnA_answer_delete(request, answer_id):
    answer = get_object_or_404(QnA_Answer, pk=answer_id)
    answer.delete()
    answer.qna.save()
    return redirect('qna:QnA_detail', qna_id=answer.qna.id)


def QnA_answer(request):
    sort_dic = {'0': '-create_date', '1': '-voter_count', '2': 'create_date'}
    pl = qna.objects
    category = request.GET.get('category', '0')
    sort = request.GET.get('sort', '0')
    page = request.GET.get('page', '1')
    pl = pl.order_by(sort_dic[sort])
    paginator = Paginator(pl, 5)
    page_obj = paginator.get_page(page)
    return render(request, 'qna/QnA_done.html', {'QnA_list': page_obj, 'page': '답변된 QnA'})
