from matplotlib import pyplot as mpl
import functions as func

#fnct = input("Enter function: ")
fnct = "1/(1+x)"

values = func.toValues(fnct)
sudd = func.intInput()
extr = func.extrInput()
        
mpl.plot(values["x"],values["y"])
mpl.show()

