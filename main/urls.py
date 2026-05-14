from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    path('semester/', views.semester, name='semester'),

    path('upload/<int:sem_no>/', views.upload_pdf, name='upload_pdf'),

    path('delete/<int:pdf_id>/', views.delete_pdf, name='delete_pdf'),
]