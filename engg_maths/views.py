from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from sympy import symbols, Eq, solve
# Create your views here.

def fetchfunc(request):
    h=request.POST['xname']
    k=request.POST['yname']
    x_lst=list(map(float,h.split()))
    y_lst=list(map(float,k.split()))
    soln=calci(x_lst,y_lst)
    print(soln)
    a,b=soln.keys()
    A=round(soln[a],4)
    B=round(soln[b],4)
    print(A,B)
    out_sol=[A,B]

    context = {
        'value_of_a' : A,
        'value_of_b' : B,
    }

    return render(request, 'solution.html', context)

def calci(X,Y):
    X_2=list(map(lambda h: h ** 2, X))
    A=np.array(X,dtype=float)
    B=np.array(Y,dtype=float)
    X_Y=A*B
    sum_x=sum(X)
    sum_y=sum(Y)
    sum_x2=sum(X_2)
    sum_xy=sum(X_Y)
    n=len(X)
    x,y = symbols('x y')
    eq1=Eq(n*x + sum_x*y - sum_y)
    eq2=Eq(sum_x*x + sum_x2*y - sum_xy)
    dic=solve((eq1,eq2), (x,y))
    return dic

