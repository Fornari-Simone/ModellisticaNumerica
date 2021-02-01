# Regole
# - Il numero n di suddivisioni deve essere variabile                                OK
# - Gli estremi di integrazione devono essere variabili in [0;+inf[                  OK
# - Deve essere indicata la funzione                                                 OK
# - Per ogni valore di n scelto, va calcolato l'errore commesso                      
# - Volendo approssimare Int[0;1](1/(1+x)dx), Quanti rettangoli sono necessari       
#   per ottenere una soluzione con una precisione alla terza cifra decimale?         

from matplotlib.pyplot import figure, bar, plot, legend, show, axvline
from functions import intInput, extrInput, toValues, pointSuddivision, calcError, extrPntMd, extrTrpz


#fnct = input("Enter function: ")
fnct = "1/(1+x)"
prmt = "ln(1+x)"


sudd = intInput()
extr = extrInput()
values = toValues(fnct, st=extr[0], end=extr[1])
suddv = pointSuddivision(sudd, extr)
forBars = extrPntMd(suddv, fnct)

figure(figsize=[10, 8])
res = 0.0
plot2 = {"x":[], "y":[]}
for i in range(len(forBars["md"])): 
  axvline(suddv[i]  ,ymax = 1/forBars["y"][i])
  axvline(suddv[i+1],ymax = 1/forBars["y"][i])
  plot2["x"].append(suddv[i])
  plot2["x"].append(suddv[i+1])
  for j in range(2): plot2["y"].append(forBars["y"][i])
  #bar(forBars["md"][i], forBars["y"][i], forBars["width"])
  res += (forBars["width"] * forBars["y"][i])
resTrpz = extrTrpz(suddv, fnct)
print("Middle point method: " + str(res))
print("Trapezoid method: " + str(resTrpz))
print("Middle point methon error: " + str(calcError(res, extr[0], extr[1])) + "%")
print("Trapezoid methon error: " + str(calcError(resTrpz, extr[0], extr[1]))+ "%")
plot(values["x"],values["y"], label=fnct)
plot(plot2["x"], plot2["y"])
legend()
show()