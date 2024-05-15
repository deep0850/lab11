from django.shortcuts import render
from django.http import HttpResponse

 
def index(request):
    return render(request, 'enter/index.html')


def about(request):
    return render(request,'enter/about.html')