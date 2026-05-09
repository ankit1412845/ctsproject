from django.urls import path
from .views import login, home, semester

urlpatterns = [
    path('', login, name='login'),
    path('home/', home, name='home'),
    path('semester/', semester, name='semester'),
]