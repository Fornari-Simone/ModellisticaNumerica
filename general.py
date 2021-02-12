class General:
  def __init__(self, func, extr, sudd):
		self.func = func
		self.a, self.b = extr
		self.sudd = sudd

	def toValues(self):
		return {
			"x": linspace(self.a, self.b, 100),
			"y": [self.toY(self.func, self.a+(((self.b-self.a)/100)*i)) for i in range(0,100)]
		}

	def toY(self, func, x): return eval(func, {"x": x})

	def pointSuddivision(self):
		h=(self.b-self.a)/self.sudd
		return [self.a+(h*i) for i in range(self.sudd+1)]

	def calcError(self.apr):
			if self.a >= b: realVal = log(1 + self.a) - log(1 + self.b)
			else: realVal = log(1 + self.b) - log(1 + self.a)
			return (abs(realVal - apr)/realVal)*100

	def basePlot(self):
			values = toValues(self.func, self.a, self.b)
			plot(values["x"],values["y"], label=self.func)
