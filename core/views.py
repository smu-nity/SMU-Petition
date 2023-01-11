from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'core/post_list.html')


def detail(request, post_id):
    print(post_id)
    return render(request, 'core/post_detail.html')


def post_create(request):
    return render(request, 'core/post_form.html')


def post_update(request, post_id):
    print(post_id)
    return render(request, 'core/post_form.html')
