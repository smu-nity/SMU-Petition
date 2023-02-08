from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from config.settings import SUCCESS_VALUE
from core.models import Petition, Comment, Answer
from django.http import HttpResponseNotAllowed

from .decorators import superuser_required
from .forms import PetitionForm, CommentForm, AnswerForm
from django.contrib import messages


def home(request):
    return render(request, 'core/home.html')


def petition_list(request):
    sort_dic = {'0': '-create_date', '1': 'create_date', '2': '-voter_count'}
    petition_list = Petition.objects.all().annotate(voter_count=Count('voter'))
    category = request.GET.get('category', '0')
    sort = request.GET.get('sort', '0')
    page = request.GET.get('page', '1')
    if category != '0':
        petition_list = petition_list.filter(category=int(category))
    petition_list = petition_list.order_by(sort_dic[sort])
    paginator = Paginator(petition_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    return render(request, 'core/petition_list.html', {'petition_list': page_obj})


def petition_detail(request, petition_id):
    petition = get_object_or_404(Petition, pk=petition_id)
    context = {'petition': petition}
    answers = Answer.objects.filter(petition=petition)
    if answers:
        context['answer'] = answers.first()
    return render(request, 'core/petition_detail.html', context)


@login_required
def petition_create(request):
    if request.method == 'POST':
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.author = request.user
            petition.save()
            return redirect('core:petition_list')
    else:
        form = PetitionForm()
    context = {'form': form}
    return render(request, 'core/petition_form.html', context)


@login_required
def petition_modify(request, petition_id):
    petition = get_object_or_404(Petition, pk=petition_id)
    if request.user != petition.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('core:petition_detail', petition_id=petition.id)
    if request.method == "POST":
        form = PetitionForm(request.POST, instance=petition)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.modify_date = timezone.now()  # 수정일시 저장
            petition.save()
            return redirect('core:petition_detail', petition_id=petition.id)
    else:
        form = PetitionForm(instance=petition)
    context = {'form': form}
    return render(request, 'core/petition_form.html', context)


@login_required
def petition_delete(request, petition_id):
    petition = get_object_or_404(Petition, pk=petition_id)
    if request.user != petition.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('core:petition_detail', petition_id=petition.id)
    petition.delete()
    return redirect('core:petition_list')


@login_required
def petition_vote(request, petition_id):
    petition = get_object_or_404(Petition, pk=petition_id)
    if request.user == petition.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    elif request.user in petition.voter.all():
        messages.error(request, '이미 추천한 글 입니다')
    else:
        petition.voter.add(request.user)
        if petition.voter.count() >= SUCCESS_VALUE:
            petition.status = 2
            petition.save()
    return redirect('core:petition_detail', petition_id=petition.id)


@login_required
def comment_create(request, petition_id):
    petition = get_object_or_404(Petition, pk=petition_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.petition = petition
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('core:petition_detail', petition_id=petition.id), comment.id))
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    return render(request, 'core/petition_detail.html', {'petition': petition, 'form': form})


@login_required
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('core:petition_detail', petition_id=comment.petition.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('core:petition_detail', petition_id=comment.petition.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    return render(request, 'core/comment_form.html', {'form': form})


@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('core:petition_detail', petition_id=comment.petition.id)


@superuser_required
def answer_create(request, petition_id):
    petition = get_object_or_404(Petition, pk=petition_id)
    if Answer.objects.filter(petition=petition):
        messages.error(request, '이미 답변한 청원입니다')
        return redirect('core:petition_detail', petition_id=petition.id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.petition = petition
            answer.save()
            petition.status = 3
            petition.save()
            return redirect('core:petition_detail', petition_id=petition.id)
    else:
        form = AnswerForm()
    return render(request, 'core/answer_form.html', {'form': form})


@superuser_required
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('core:petition_detail', petition_id=answer.petition.id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'core/answer_form.html', {'form': form})


@superuser_required
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    answer.petition.status = 1
    if answer.petition.voter.count() >= SUCCESS_VALUE:
        answer.petition.status = 2
    answer.petition.save()
    return redirect('core:petition_detail', petition_id=answer.petition.id)
