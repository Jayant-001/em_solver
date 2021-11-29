from django.shortcuts import render

# Create your views here.
def fetchfunc(req):
    x=req.POST.get('xname','error')
    y=req.POST.get('yname','error')
    x_lst=list(map(int,x.split()))
    y_lst=list(map(int,y.split()))
    a=b=0
    return a,b;