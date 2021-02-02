from matplotlib.pyplot import figure, bar, plot, legend, show, axvline, ylim, rcParams, title
from functions import intInput, extrInput, toValues, pointSuddivision, calcError, extrPntMd, sumTrpz, sumPntMd, percent


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

res = sumPntMd(forBars["y"],forBars["width"])
resTrpz = sumTrpz(suddv, fnct)
print("Middle point method: " + str(res))
print("Trapezoid method: " + str(resTrpz))
print("Middle point method error: " + str(calcError(res, extr[0], extr[1])) + "%")
print("Trapezoid method error: " + str(calcError(resTrpz, extr[0], extr[1]))+ "%")
legend()
show()