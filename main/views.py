from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_page(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        # REGISTER
        if form_type == "register":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect("/?login=true")

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            messages.success(request, "Registration successful. Please login.")
            return redirect("/?login=true")

        # LOGIN
        elif form_type == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("login")

    return render(request, "main/login.html")


def home(request):
    return render(request, "main/home.html")

def semester(request):
    return render(request, "main/semester.html")

from .models import PDFUpload

def upload_pdf(request, sem_no):

    if request.method == "POST":
        pdf_file = request.FILES.get("pdf_file")

        if pdf_file:
            PDFUpload.objects.create(
                semester=sem_no,
                pdf_file=pdf_file
            )

        return redirect("upload_pdf", sem_no=sem_no)

    pdfs = PDFUpload.objects.filter(semester=sem_no)

    return render(request, "main/upload.html", {
        "sem_no": sem_no,
        "pdfs": pdfs
    })

def delete_pdf(request, pdf_id):
    pdf = PDFUpload.objects.get(id=pdf_id)
    sem_no = pdf.semester
    pdf.delete()
    return redirect("upload_pdf", sem_no=sem_no)