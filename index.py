from matplotlib import pyplot as mpl
import functions as func

#fnct = input("Enter function: ")
fnct = "1/(1+x)"

values = func.toValues(fnct)
sudd = func.intInput()
extr = func.extrInput()
print(extr)
        
mpl.plot(values["x"],values["y"])
mpl.show()

