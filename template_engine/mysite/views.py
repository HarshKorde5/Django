from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Ganpati Bappa Morya')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('Mangal Murti Morya')
    return render(request, 'mysite/about.html')

def contact(request):
    # return HttpResponse("Hello World! This is the contact page, Thank YOU!")
    return render(request, 'mysite/contact.html')
