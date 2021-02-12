class General:
  def __init__(self, func, extr):
		self.func = func
		self.a, self.b = extr

	def toValues():
		return {
			"x": linspace(self.a, self.b, 100),
			"y": [eval(self.func, {"x": self.a+(((self.b-self.a)/100)*i)}) for i in range(0,100)]
		}

	# def toY(func, x): return eval(func, {"x": x})

	def pointSuddivision(sudd, extr):
		h=(extr[1]-extr[0])/sudd
		return [extr[0]+(h*i) for i in range(sudd+1)]

	def calcError(apr, a, b):
			if a >= b: realVal = log(1 + a) - log(1 + b)
			else: realVal = log(1 + b) - log(1 + a)
			return (abs(realVal - apr)/realVal)*100

	def basePlot(func, extr):
			values = toValues(func, extr[0], extr[1])
			plot(values["x"],values["y"], label=func)
