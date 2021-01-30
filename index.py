# Regole
# - Il numero n di suddivisioni deve essere variabile                                OK
# - Gli estremi di integrazione devono essere variabili in [0;+inf[                  OK
# - Deve essere indicata la funzione                                                 OK
# - Per ogni valore di n scelto, va calcolato l'errore commesso                      
# - Volendo approssimare Int[0;1](1/(1+x)dx), Quanti rettangoli sono necessari       
#   per ottenere una soluzione con una precisione alla terza cifra decimale?         

from matplotlib import pyplot as mpl
import functions as func


#fnct = input("Enter function: ")
fnct = "1/(1+x)"


sudd = func.intInput()
extr = func.extrInput()
values = func.toValues(fnct, st=extr[0], end=extr[1])
suddv = func.pointSuddivision(sudd, extr)
forBars = func.extrPntMd(suddv, fnct)

mpl.figure(figsize=[10, 8])
for i in range(len(forBars["md"])): 
  mpl.bar(forBars["md"][i], forBars["y"][i])
mpl.plot(values["x"],values["y"], label=fnct)
mpl.legend()
mpl.show()

