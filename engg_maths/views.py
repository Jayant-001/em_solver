from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
<<<<<<< HEAD
def fetchfunc(req):
    x=req.POST.get('xname','error')
    y=req.POST.get('yname','error')
    x_lst=list(map(int,x.split()))
    y_lst=list(map(int,y.split()))
    a=b=0

    print(x_lst)
    print(y_lst)


    return a,b
=======
def fetchfunc(request):
    x=request.POST['xname']
    y=request.POST['yname']
    # x_lst=list(map(int,x.split()))
    # y_lst=list(map(int,y.split()))
    print(x,y)
    return HttpResponse("<h1>hello</h1>");
>>>>>>> 688c50e2603e8b02c023b25185b8db9222434a10
