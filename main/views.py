from django.shortcuts import render


def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')

def researchprojects(request):
    return render(request, 'researchprojects.html')

def project1(request):
    return render(request, 'researchprojects/project1.html')

def project2(request):
    return render(request, 'researchprojects/project2.html')

def project3(request):
    return render(request, 'researchprojects/project3.html')

def project4(request):
    return render(request, 'researchprojects/project4.html')

def project5(request):
    return render(request, 'researchprojects/project5.html')

def publications(request):
    return render(request, 'publications.html')

def courses(request):
    return render(request, 'courses.html')

def software(request):
    return render(request, 'software.html')

def bio(request):
    return render(request, 'bio.html')
