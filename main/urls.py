from django.urls import path
from .views import login, home, semester, civil, electrical, mechanical

urlpatterns = [
    path('', login, name='login'),
    path('home/', home, name='home'),
    path('semester/', semester, name='semester'),
    path('civil/', civil, name='civil'),
    path('electrical/', electrical, name='electrical'), 
    path('mechanical/', mechanical, name='mechanical'),

]