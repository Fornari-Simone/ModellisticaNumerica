from matplotlib.pyplot import figure, bar, plot, legend, show, axvline, ylim, rcParams, title
from functions import intInput, extrInput, toValues, pointSuddivision 
from functions import calcError, extrPntMd, sumTrpz, sumPntMd, percent
from functions import sumSimp, calcFunc


#fnct = input("Enter function: ")
fnct = "1/(1+x)"
prmt = "ln(1+x)"


sudd = intInput()
extr = extrInput()
values = toValues(fnct, st=extr[0], end=extr[1])
suddv = pointSuddivision(sudd, extr)
forBars = extrPntMd(suddv, fnct)

plot2 = {
  "mp": {"x":[], "y":[]},
  "tr": {"x":[], "y":[]}
}

rcParams["figure.figsize"]=(10, 8)

figure(1)
ylim(0,1)
title("Middle point Method")
for idx, i in enumerate(forBars["y"]): 
  axvline(suddv[idx]  ,ymax = i)
  axvline(suddv[idx+1],ymax = i)
  plot2["mp"]["x"].append(suddv[idx])
  plot2["mp"]["x"].append(suddv[idx+1])
  for j in range(2): plot2["mp"]["y"].append(i)
plot(values["x"],values["y"], label=fnct)
plot(plot2["mp"]["x"], plot2["mp"]["y"])

figure(2)
ylim(0,1)
title("Trapezoid Method")
for i in suddv:
  axvline(i  ,ymax = eval(fnct, {"x":i}))
  plot2["tr"]["x"].append(i)
  plot2["tr"]["y"].append(eval(fnct, {"x":i}))
plot(values["x"],values["y"], label=fnct)
plot(plot2["tr"]["x"], plot2["tr"]["y"])

figure(3)
ylim(0,1)
title("Cavalieri-Simpson method")
fnctSimp = calcFunc(fnct, extr[0], extr[1])
valueSimp = toValues(fnctSimp, st=extr[0], end=extr[1])
plot(valueSimp["x"],valueSimp["y"], label=fnct)

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