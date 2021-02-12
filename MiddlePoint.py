from general import General
from matplotlib.pyplot import figure, ylim, title, axvline

class MiddlePoint(General):
	def __init__(self, func, extr, sudd):
		super(func, extr, sudd).__init__()
    	self.suddv = super.pointSuddivision()
    	epm = self.extrPntMd()
    	self.width = epm["width"]
    	self.y = epm["y"]

	def calcError(self):
    	return super.calcError(self.sumPntMd())

	def extrPntMd(self):
    	return {
			"y": [toY(self.func, (self.suddv[i]+self.suddv[i+1])/2) for i in range(len(self.suddv)-1)],
			"width": self.suddv[1] - self.suddv[0]
		}

  def sumPntMd(self): 
    return sum([self.width*i for i in self.y])

  def plotMd(self, nfig):
    plt = {"x": [], "y": []}
    figure(nfig)
    figure.figsize = (8,6)
    ylim(0,1)
    title("Middle point Method")
    for idx, i in enumerate(forBarsY): 
      axvline(self.suddv[idx]  ,ymax = i)
      axvline(self.suddv[idx+1],ymax = i)
      plt["x"].append(self.suddv[idx])
      plt["x"].append(self.suddv[idx+1])
      for j in range(2): plt["y"].append(i)
    basePlot()
    plot(plt["x"], plt["y"])