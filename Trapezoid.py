from general import General
from matplotlib.pyplot import figure, ylim, title, axvline, plot

class Trapezoid(General):
	def __init__(self, func, extr, sudd):
		super().__init__(func, extr, sudd)

	def calcError(self):
		return super().calcError(self.summ())

	def summ(self):
		h = (self.suddv[-1] - self.suddv[0])/(len(self.suddv)-1)
		return (h/2)*sum([(eval(self.func, {"x": self.suddv[i]}) + eval(self.func, {"x": self.suddv[i+1]})) for i in range(len(self.suddv)-1)])

	def drawPlot(self, nfig):
		plt = {"x": [], "y":[]}
		figure(nfig)
		figure.figsize = (8,6)
		ylim(0,1)
		title("Trapezoid Method")
		for i in self.suddv:
			axvline(i  ,ymax = eval(self.func, {"x": i}))
			plt["x"].append(i)
			plt["y"].append(eval(self.func, {"x": i}))
		super().basePlot()
		plot(plt["x"], plt["y"])
