from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def signup(request):
    return render(request, 'accounts/signup.html')