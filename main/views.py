from django.shortcuts import render


def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')
def publications(request):
    return render(request, 'publications.html')

def courses(request):
    return render(request, 'courses.html')

def software(request):
    return render(request, 'software.html')

def bio(request):
    return render(request, 'bio.html')
