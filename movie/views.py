from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    ##return HttpResponse('<h1>Welcome to my page</h1>')
    return render(request, 'home.html', {'name' : 'Luis Felipe'})

def about(request):
    ##return HttpResponse('<h1>Welcome to my page</h1>')
    return render(request, 'about.html')