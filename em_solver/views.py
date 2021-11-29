from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputData

def home(req) :
    return render(req, 'home.html')

def math(req) :
    return render(req, 'math.html')

def dstl(req) :
    return render(req, 'dstl.html')

def test(req) :
    return render(req, 'test.html', {'name':'/test'})

def showFormData(request):
    fm = InputData()
    return render(request, 'enro')
