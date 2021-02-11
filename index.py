from matplotlib.pyplot import legend, show
from functions import intInput, extrInput, toValues, pointSuddivision, calcError, toY
from functions import extrPntMd, sumPntMd, plotMd
from functions import sumTrpz, plotTrpz
from functions import sumSimp, calcFunc, plotSimp


#fnct = input("Enter function: ")
fnct = "1/(1+x)"
prmt = "ln(1+x)"


sudd = intInput()
extr = extrInput()
suddv = pointSuddivision(sudd, extr)
forBars = extrPntMd(suddv, fnct)

plotMd(1, suddv, forBars["y"], fnct, extr)
plotTrpz(2, suddv, fnct, extr)
plotSimp(3, suddv, fnct, extr)

res = sumPntMd(forBars["y"],forBars["width"])
resTrpz = sumTrpz(suddv, fnct)
resSimp = sumSimp(suddv, fnct)
print(f"Middle point method: {str(res)}")
print(f"Trapezoid method: {str(resTrpz)}")
print(f"Cavalieri-Simpson method: {str(resSimp)}")
print(f"Middle point method error: {str(calcError(res, extr[0], extr[1]))} %")
print(f"Trapezoid method error: {str(calcError(resTrpz, extr[0], extr[1]))} %")
print(f"Cavalieri-Simpson method error: {str(calcError(resSimp, extr[0], extr[1]))} %")
legend()
show()