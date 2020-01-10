class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __repr__(self):
		return "Low is: {}, High is {}".format(self.current, self.high)

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration



c = Counter(0,10)
a = iter(c)
print(a)


# for x in Counter(50,70):
# 	print(x)