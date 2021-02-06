from numpy import linspace as linspace
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
    return (h/2)*sum([(eval(func, {"x":suddv[i]})+eval(func, {"x":suddv[i+1]})) for i in range(len(suddv)-1)])