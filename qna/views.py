from django.core.paginator import Paginator
from django.shortcuts import render
from qna.models import Question


def question_list(request):
    ql = Question.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(ql, 5)
    page_obj = paginator.get_page(page)
    return render(request, 'qna/question_list.html', {'question_list': page_obj})


def question_detail(request, question_id):
    print(question_id)
    return render(request, 'qna/question_detail.html')
