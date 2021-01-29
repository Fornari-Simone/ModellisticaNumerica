import re

def toValues(func, st=0, end=100, step=1):
    try:
        return {
            "x":[i for i in range(st, end, 1 if type(step) == float else step)],
            "y":[eval(func, {"x":i}) for i in range(st, end, 1 if type(step) == float else step)]
        }
    except:
        print("Wrong input")
        return toValues(input("Enter function: "), st, end, step)

def intInput():
    try: return int(input("Enter suddivision: "))
    except:
        print("Wrong input")
        return intInput()

def extrInput():
    extr = input("Enter interval: ")
    if re.search("(\d+\:\d+)", extr) != None :
        arr = [int(i) for i in re.findall("(\d+\:\d+)", extr)[0].split(":")]
        arr.sort()
        return arr
    else:
        print("Wrong input")
        return extrInput()
        
