class UpdateQueue:
	def __init__(self, value=0):
		self.value = value

	def decrement(self):
		self.value -= 10

	def increment(self):
		self.value += 10
	def getvalue(self):
		return self.value

	def __str__(self):
		return "The counter value is %d" % self.value
