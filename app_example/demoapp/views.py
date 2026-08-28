from django.shortcuts import render

# Create your views here.
def demohome(request):
    return render(request, 'demoapp/index.html')