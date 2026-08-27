from django.http import HttpResponse

def home(request):
    return HttpResponse("Ganpati Bappa Morya!")

def about(request):
    return HttpResponse("Mangal Murti Morya!")

def contact(request):
    return HttpResponse("Hello World! This is the contact page, Thank YOU!")