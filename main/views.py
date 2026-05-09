from django.shortcuts import render

def login(request):
    return render(request, 'main/login.html')

def home(request):
    return render(request, 'main/home.html')

def semester(request):
    return render(request, 'main/semester.html')