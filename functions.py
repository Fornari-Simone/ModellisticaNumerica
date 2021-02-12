import re

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
            return (arr[0], arr[1])
    print("Wrong input")
    return extrInput()
