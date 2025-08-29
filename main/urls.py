from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('researchprojects/', views.researchprojects, name='researchprojects'),
    path('researchprojects/project1/', views.project1, name='project1'),
    path('researchprojects/project2/', views.project2, name='project2'),
    path('researchprojects/project3/', views.project3, name='project3'),
    path('researchprojects/project4/', views.project4, name='project4'),
    path('researchprojects/project5/', views.project5, name='project5'),  
    path('publications/', views.publications, name='publications'),
    path('courses/', views.courses, name='courses'),
    path('software/', views.software, name='software'),
    path('bio/', views.bio, name='bio'),
]
