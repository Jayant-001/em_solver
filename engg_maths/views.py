from math import log10
from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from sympy import symbols, Eq, solve
from engg_maths.models import MathData
import ast

# Create your views here.



def fetchfunc(request):
    h = request.POST['xname']
    k = request.POST['yname']
    ch = request.POST['inputData']
    print(ch)
    x_lst = list(map(float, h.split()))
    y_lst = list(map(float, k.split()))
    if(ch == "1"):
        soln, x2_lst, xy_lst = straight(x_lst, y_lst)
        a, b = soln.keys()
        A = "{0:.4f}".format(soln[a])
        B = "{0:.4f}".format(soln[b])
        context = {'value_of_a': A, 'value_of_b': B}
        print(A, B)
        master_lst = []
        for i in range(len(x_lst)):
            lst = []
            lst.append(x_lst[i])
            lst.append(y_lst[i])
            lst.append(x2_lst[i])
            lst.append(xy_lst[i])
            master_lst.append(lst)
        lst = [sum(x_lst), sum(y_lst), sum(x2_lst), sum(xy_lst)]
        master_lst.append(lst)
        context['tab'] = master_lst
        # data = MathData.objects.all()
        # for d in data:
        #     X=ast.literal_eval(d.x_list)
        #     Y=ast.literal_eval(d.y_list)
        #     X2=ast.literal_eval(d.x2_list)
        #     XY=ast.literal_eval(d.xy_list)
        #     # print(d.x_list)
        #     # print(d.y_list)
        #     # print(d.x2_list)
        #     # print(d.xy_list)
        #     print("-----------------------")

        # math_data = MathData(x_list=x_lst, y_list=y_lst,
        #                      x2_list=x2_lst, xy_list=xy_lst)
        # math_data.save()

    elif(ch == "2"):
        soln,x2_lst,x3_lst,x4_lst,xy_lst,x2y_lst= parabola(x_lst, y_lst)
        a, b, c = soln.keys()
        A = "{0:.4f}".format(soln[a])
        B = "{0:.4f}".format(soln[b])
        C = "{0:.4f}".format(soln[c])
        context = {'value_of_a': ("A is", A), 'value_of_b': ("B is", B), 'value_of_c': ("C is", C)}
        print(A, B, C)
        master_lst = []
        for i in range(len(x_lst)):
            lst = []
            lst.append(x_lst[i])
            lst.append(y_lst[i])
            lst.append(x2_lst[i])
            lst.append(x3_lst[i])
            lst.append(x4_lst[i])
            lst.append(xy_lst[i])
            lst.append(x2y_lst[i])
            master_lst.append(lst)
        lst = [sum(x_lst), sum(y_lst),sum(x2_lst), sum(x3_lst),sum(x4_lst), sum(xy_lst),sum(x2y_lst)]
        master_lst.append(lst)
        context['tab'] = master_lst
    elif(ch=="3"):
        soln,Y_lst,x2_lst,xy_lst=exp(x_lst,y_lst)
        a, b = soln.keys()
        A = "{0:.4f}".format(soln[a])
        B = "{0:.4f}".format(soln[b])
        context = {'value_of_a': A, 'value_of_b': B}
        print(A, B)
        master_lst = []
        for i in range(len(x_lst)):
            lst = []
            lst.append(x_lst[i])
            lst.append(y_lst[i])
            lst.append(Y_lst[i])
            lst.append(x2_lst[i])
            lst.append(xy_lst[i])
            master_lst.append(lst)
        lst = [sum(x_lst), sum(y_lst),sum(Y_lst), sum(x2_lst), sum(xy_lst)]
        master_lst.append(lst)
        context['tab'] = master_lst
    print(soln)
    return render(request, 'solution.html', context)


def straight(X, Y):
    x2 = list(map(lambda h: h ** 2, X))
    A = np.array(X, dtype=float)
    B = np.array(Y, dtype=float)
    xy = A*B
    sum_x = sum(X)
    sum_y = sum(Y)
    sum_x2 = sum(x2)
    sum_xy = sum(xy)
    n = len(X)
    x, y = symbols('x y')
    eq1 = Eq(n*x + sum_x*y - sum_y)
    eq2 = Eq(sum_x*x + sum_x2*y - sum_xy)
    dic = solve((eq1, eq2), (x, y))
    return dic, x2, xy


def parabola(X, Y):
    x2 = list(map(lambda h: h ** 2, X))
    x3 = list(map(lambda h: h ** 3, X))
    x4 = list(map(lambda h: h ** 4, X))
    A = np.array(X, dtype=float)
    B = np.array(Y, dtype=float)
    C = A*A
    xy = A*B
    x2y = C*B
    sum_x = sum(X)
    sum_y = sum(Y)
    sum_x2 = sum(x2)
    sum_x3 = sum(x3)
    sum_x4 = sum(x4)
    sum_xy = sum(xy)
    sum_x2y = sum(x2y)
    n = len(X)
    x, y, z = symbols('x y z')
    eq1 = n*x + sum_x*y + sum_x2*z - sum_y
    eq2 = sum_x*x + sum_x2*y + sum_x3*z - sum_xy
    eq3 = sum_x2*x + sum_x3*y + sum_x4*z - sum_x2y
    dic = solve((eq1, eq2, eq3), (x, y, z))
    return dic,x2,x3,x4,xy,x2y


def exp(X,Y):
    y=list(map(lambda h: log10(h),Y))
    x2 = list(map(lambda h: h ** 2, X))
    A = np.array(X, dtype=float)
    B = np.array(y, dtype=float)
    C = A*A
    xy = A*B
    sum_x = sum(X)
    sum_y = sum(y)
    sum_x2 = sum(x2)
    sum_xy = sum(xy)
    n = len(X)
    x, y = symbols('x y')
    eq1 = Eq(n*x + sum_x*y - sum_y)
    eq2 = Eq(sum_x*x + sum_x2*y - sum_xy)
    dic = solve((eq1, eq2), (x, y))
    return dic, y,x2,xy;