from matplotlib import pyplot as mpl
import numpy as npy
import re

def toValues(func, st=0, end=100,):
    return {
        "x": npy.linspace(st, end, 100),
        "y": [eval(func, {"x":((end-st)/100)*i}) for i in range(0,100)]
    }

def intInput():
    try: return int(input("Enter suddivision: "))
    except:
        print("Wrong input")
        return intInput()

def extrInput():
    extr = input("Enter interval: ")
    if re.search("(\d+\;\d+)", extr) != None :
        arr = [int(i) for i in re.findall("(\d+\;\d+)", extr)[0].split(";")]
        if arr[0] > -1 or arr[1] > -1 : 
            arr.sort()
            return arr
    print("Wrong input")
    return extrInput()

def pointSuddivision(sudd, extr):
    h=(extr[1]-extr[0])/sudd
    return [extr[0]+(h*i) for i in range(sudd+1)]

def extrPntMd(suddv, func):
    return {
        "md": [(suddv[i]+suddv[i+1])/2 for i in range(len(suddv)-1)],
        "y": [eval(func, {"x": i}) for i in range(len(suddv)-1)],
        "width": suddv[1] - suddv[0]
    }
        

