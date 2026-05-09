from django.shortcuts import render

def login(request):
    return render(request, 'main/login.html')

def home(request):
    return render(request, 'main/home.html')

def semester(request):
    return render(request, 'main/semester.html')

def civil(request):
    return render(request, 'main/civil.html')

def electrical(request):
    return render(request, 'main/electrical.html')

def mechanical(request):
    return render(request, 'main/mechanical.html')