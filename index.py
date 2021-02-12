from matplotlib.pyplot import legend, show
from functions import intInput, extrInput
from MiddlePoint import MiddlePoint
from Trapezoid import Trapezoid
from Simpson import Simpson

fnct = "1/(1+x)"

sudd = intInput()
extr = extrInput()

middle = MiddlePoint(fnct, extr, sudd)
trpz = Trapezoid(fnct, extr, sudd)
simp = Simpson(fnct, extr, sudd)

middle.drawPlot(1)
trpz.drawPlot(2)
simp.drawPlot(3)

print(f"Middle point method: {str(middle.summ())}")
print(f"Trapezoid method: {str(trpz.summ())}")
print(f"Cavalieri-Simpson method: {str(simp.summ())}")
print(f"Middle point method error: {str(middle.calcError())} %")
print(f"Trapezoid method error: {str(trpz.calcError())} %")
print(f"Cavalieri-Simpson method error: {str(simp.calcError())} %")
legend()
show()