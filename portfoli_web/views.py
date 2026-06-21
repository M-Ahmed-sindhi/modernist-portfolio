from django.shortcuts import render

# Create your views here

def first_page(request):
    return render(request, 'first_page.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')