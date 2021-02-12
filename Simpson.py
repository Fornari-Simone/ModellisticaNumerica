from general import General
from numpy import mat
from numpy.linalg import solve 
from matplotlib.pyplot import figure, ylim, title, axvline, plot

class Simpson(General):
	def __init__(self, func, extr, sudd):
		super().__init__(func, extr, sudd)

	def calcError(self):
		return super().calcError(self.summ())

	def summ(self):
		hs = (self.suddv[1]-self.suddv[0])/3
		return sum([hs*(
			eval(self.func, {"x": self.suddv[i]}) 
			+ (4*(eval(self.func, {"x": self.suddv[i+1]}))) 
			+ eval(self.func, {"x": self.suddv[i+2]})) for i in range(0, len(self.suddv)-2, 2)])

	def calcFunc(self):
		x = mat(f"{self.a**2} {self.a} 1; {self.b**2} {self.b} 1; {((self.a+self.b)/2)**2} {(self.a+self.b)/2} 1")
		y = mat(str(eval(self.func, {"x": self.a})) + "; " + 
				str(eval(self.func, {"x": self.b})) + "; " + 
				str(eval(self.func, {"x": (self.a+self.b)/2}))
			)
		sis = solve(x, y).tolist()
		return f"({sis[0][0]})*(x**2)+({sis[1][0]})*(x)+({sis[2][0]})"

	def drawPlot(self, nfig):
		figure(nfig)
		figure.figsize = (8,6)
		ylim(0,1)
		title("Cavalieri-Simpson method")
		fnctSimp = self.calcFunc()
		valueSimp = super().toValues(fnctSimp)
		super().basePlot()
		plot(valueSimp["x"],valueSimp["y"])
		for i in self.suddv: axvline(i  ,ymax = eval(fnctSimp, {"x": i}))
