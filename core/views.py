from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about_me(request):
    return render(request, 'core/about-me.html')

def contact(request):
    return render(request, 'core/contact.html')