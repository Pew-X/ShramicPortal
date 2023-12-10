
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return render(request,'index.html')

def registration(request):

    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    return render(request, 'worker.html')