from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('publications/', views.publications, name='publications'),
    path('courses/', views.courses, name='courses'),
    path('software/', views.software, name='software'),
    path('bio/', views.bio, name='bio'),
]
