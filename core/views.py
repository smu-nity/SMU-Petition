from django.shortcuts import render
from .models import Question


def home(request):
    return render(request, 'home.html')


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'core/post_list.html', context)


def detail(request, post_id, question_id):
    print(post_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'core/post_detail.html', 'core/question_detail.html', context)


def post_create(request):
    return render(request, 'core/post_form.html')


def post_update(request, post_id):
    print(post_id)
    return render(request, 'core/post_form.html')
