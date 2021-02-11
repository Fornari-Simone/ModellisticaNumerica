from numpy import linspace, mat
from numpy.linalg import solve 
from math import log
import re

# General
def toValues(func, st=0, end=100,):
    return {
        "x": linspace(st, end, 100),
        "y": [toY(func, st+(((end-st)/100)*i)) for i in range(0,100)]
    }

def toY(func, x):
    return eval(func, {"x": x})

def intInput():
    try: return int(input("Enter suddivision: "))
    except:
        print("Wrong input")
        return intInput()

def extrInput():
    extr = input("Enter interval (a;b): ")
    if re.search("(\d+\;\d+)", extr) != None :
        arr = [int(i) for i in re.findall("(\d+\;\d+)", extr)[0].split(";")]
        if arr[0] > -1 and arr[1] > -1:
            arr.sort()
            return arr
    print("Wrong input")
    return extrInput()

def pointSuddivision(sudd, extr):
    h=(extr[1]-extr[0])/sudd
    return [extr[0]+(h*i) for i in range(sudd+1)]

def calcError(apr, a, b):
    if a >= b: realVal = log(1 + a) - log(1 + b)
    else: realVal = log(1 + b) - log(1 + a)
    return (abs(realVal - apr)/realVal)*100

def percent(ymin, ymax, yactual):
    # ymax-ymin : 100 = yactual:x
    return (yactual*100)/(ymax-ymin)


# Middle Point
def extrPntMd(suddv, func):
    return {
        "md": [(suddv[i]+suddv[i+1])/2 for i in range(len(suddv)-1)],
        "y": [toY(func, (suddv[i]+suddv[i+1])/2) for i in range(len(suddv)-1)],
        "width": suddv[1] - suddv[0]
    }

def sumPntMd(y, width):
    return sum([width*i for i in y])

# trapezoid method
def sumTrpz(suddv, func):
    h = (suddv[-1] - suddv[0])/(len(suddv)-1)
    return (h/2)*sum([(toY(func, suddv[i])+toY(func, suddv[i+1])) for i in range(len(suddv)-1)])

# Simpson method
def sumSimp(suddv, func):
    hs = (suddv[1]-suddv[0])/3
    return sum([hs*(toY(func, suddv[i]) + (4*(toY(func, suddv[i+1]))) + toY(func, suddv[i+2])) for i in range(0, len(suddv)-2, 2)])

def calcFunc(func, a, b):
    # A(ax)^2 + B(ax) + C = ay
    # A(bx)^2 + B(bx) + C = by
    # A{[(a+b)/2]x}^2 + B{[(a+b)/2]x} + C = [(a+b)/2]y

    x = mat(f"{a**2} {a} 1; {b**2} {b} 1; {((a+b)/2)**2} {(a+b)/2} 1")
    y = mat(f"{toY(func, a)}; {toY(func, b)}; {toY(func, (a+b)/2)}")
    sis = solve(x, y).tolist()
    return f"({sis[0][0]})*(x**2)+({sis[1][0]})*(x)+({sis[2][0]})"