from django.shortcuts import render
from django.http import HttpResponse

def home(req) :
    return render(req, 'home.html')

def math(req) :
    return render(req, 'math.html')

def dstl(req) :
    return render(req, 'dstl.html')

def test(req) :
    return render(req, 'test.html')

