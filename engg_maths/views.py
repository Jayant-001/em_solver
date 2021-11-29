from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fetchfunc(request):
    x=request.POST['xname']
    y=request.POST['yname']
    # x_lst=list(map(int,x.split()))
    # y_lst=list(map(int,y.split()))
    print(x,y)
    return HttpResponse("<h1>hello</h1>");