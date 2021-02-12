from general import General
from matplotlib.pyplot import figure, ylim, title, axvline, plot

class MiddlePoint(General):
	def __init__(self, func, extr, sudd):
		super().__init__(func, extr, sudd)
		epm = self.extr()
		self.width = epm["width"]
		self.y = epm["y"]

	def calcError(self):
		return super().calcError(self.summ())

	def extr(self):
		return {
			"y": [
				eval(self.func, {"x": (self.suddv[i]+self.suddv[i+1])/2}) for i in range(len(self.suddv)-1)
			],
			"width": self.suddv[1] - self.suddv[0]
		}

	def summ(self): return sum([self.width*i for i in self.y])

	def drawPlot(self, nfig):
		plt = {"x": [], "y": []}
		figure(nfig)
		figure.figsize = (8,6)
		ylim(0,1)
		title("Middle point Method")
		for idx, i in enumerate(self.y): 
			axvline(self.suddv[idx]  ,ymax = i)
			axvline(self.suddv[idx+1],ymax = i)
			plt["x"].append(self.suddv[idx])
			plt["x"].append(self.suddv[idx+1])
			for j in range(2): plt["y"].append(i)
		super().basePlot()
		plot(plt["x"], plt["y"])