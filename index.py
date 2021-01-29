from matplotlib import pyplot as mpl

def toValues(func):
    x = []
    y = []
    for i in range(0,100):
        x.append(i)
        y.append(eval(func.replace("x", "("+str(i)+")")))
    return {"x": x, "y": y}

values = toValues("x**2")

mpl.plot(values["x"],values["y"])
mpl.show()

