from numpy import linspace, mat
from numpy.linalg import solve 
from math import log
from matplotlib.pyplot import figure, plot, axvline, ylim, title
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

def basePlot(func, extr):
    values = toValues(func, extr[0], extr[1])
    plot(values["x"],values["y"], label=func)

# Middle Point
def extrPntMd(suddv, func):
    return {
        "md": [(suddv[i]+suddv[i+1])/2 for i in range(len(suddv)-1)],
        "y": [toY(func, (suddv[i]+suddv[i+1])/2) for i in range(len(suddv)-1)],
        "width": suddv[1] - suddv[0]
    }

def sumPntMd(y, width):
    return sum([width*i for i in y])

def plotMd(nfig, suddv, forBarsY, func, extr):
    plt = {"x": [], "y": []}
    figure(nfig)
    figure.figsize = (8,6)
    ylim(0,1)
    title("Middle point Method")
    for idx, i in enumerate(forBarsY): 
        axvline(suddv[idx]  ,ymax = i)
        axvline(suddv[idx+1],ymax = i)
        plt["x"].append(suddv[idx])
        plt["x"].append(suddv[idx+1])
        for j in range(2): plt["y"].append(i)
    basePlot(func, extr)
    plot(plt["x"], plt["y"])

# trapezoid method
def sumTrpz(suddv, func):
    h = (suddv[-1] - suddv[0])/(len(suddv)-1)
    return (h/2)*sum([(toY(func, suddv[i])+toY(func, suddv[i+1])) for i in range(len(suddv)-1)])

def plotTrpz(nfig, suddv, func, extr):
    plt = {"x": [], "y":[]}
    figure(nfig)
    figure.figsize = (8,6)
    ylim(0,1)
    title("Trapezoid Method")
    for i in suddv:
        axvline(i  ,ymax = toY(func, i))
        plt["x"].append(i)
        plt["y"].append(toY(func, i))
    basePlot(func, extr)
    plot(plt["x"], plt["y"])

# Simpson method
def sumSimp(suddv, func):
    hs = (suddv[1]-suddv[0])/3
    return sum([hs*(toY(func, suddv[i]) + (4*(toY(func, suddv[i+1]))) + toY(func, suddv[i+2])) for i in range(0, len(suddv)-2, 2)])

def calcFunc(func, a, b):
    x = mat(f"{a**2} {a} 1; {b**2} {b} 1; {((a+b)/2)**2} {(a+b)/2} 1")
    y = mat(f"{toY(func, a)}; {toY(func, b)}; {toY(func, (a+b)/2)}")
    sis = solve(x, y).tolist()
    return f"({sis[0][0]})*(x**2)+({sis[1][0]})*(x)+({sis[2][0]})"

def plotSimp(nfig, suddv, func, extr):
    figure(nfig)
    figure.figsize = (8,6)
    ylim(0,1)
    title("Cavalieri-Simpson method")
    fnctSimp = calcFunc(func, extr[0], extr[1])
    valueSimp = toValues(fnctSimp, st=extr[0], end=extr[1])
    basePlot(func, extr)
    plot(valueSimp["x"],valueSimp["y"])
    for i in suddv: axvline(i  ,ymax = toY(fnctSimp, i))