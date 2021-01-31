# Regole
# - Il numero n di suddivisioni deve essere variabile                                OK
# - Gli estremi di integrazione devono essere variabili in [0;+inf[                  OK
# - Deve essere indicata la funzione                                                 OK
# - Per ogni valore di n scelto, va calcolato l'errore commesso                      
# - Volendo approssimare Int[0;1](1/(1+x)dx), Quanti rettangoli sono necessari       
#   per ottenere una soluzione con una precisione alla terza cifra decimale?         

from matplotlib.pyplot import figure, bar, plot, legend, show
from functions import intInput, extrInput, toValues, pointSuddivision, extrPntMd
from scipy import integrate


#fnct = input("Enter function: ")
fnct = "1/(1+x)"

sudd = intInput()
extr = extrInput()
values = toValues(fnct, st=extr[0], end=extr[1])
suddv = pointSuddivision(sudd, extr)
forBars = extrPntMd(suddv, fnct)

figure(figsize=[10, 8])
res = 0.0
for i in range(len(forBars["md"])): 
  bar(forBars["md"][i], forBars["y"][i], forBars["width"])
  res += (forBars["width"] * forBars["y"][i])

print("the result is: " + str(res))
plot(values["x"],values["y"], label=fnct)
legend()
show()

