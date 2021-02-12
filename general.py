from matplotlib.pyplot import plot
from math import log
from numpy import linspace

class General:
	def __init__(self, func, extr, sudd):
		self.func = func
		self.a, self.b = extr
		self.sudd = sudd
		self.suddv = self.pointSuddivision()

	def toValues(self, func):
		return {
			"x": linspace(self.a, self.b, 100),
			"y": [eval(func, {"x": self.a+(((self.b-self.a)/100)*i)}) for i in range(0,100)]
		}

	def pointSuddivision(self):
		h=(self.b-self.a)/self.sudd
		return [self.a+(h*i) for i in range(self.sudd+1)]

	def calcError(self, apr):
		if self.a >= self.b: realVal = log(1 + self.a) - log(1 + self.b)
		else: realVal = log(1 + self.b) - log(1 + self.a)
		return (abs(realVal - apr)/realVal)*100

	def basePlot(self):
		values = self.toValues(self.func)
		plot(values["x"],values["y"], label=self.func)
