### helpers 
import random
class Position:
	def __init__(self, value):
		self.value = value
		if self.value == 0:
			self.possible = [i for i in range(1, 10)]
			random.shuffle(self.possible)
		else:
			self.possible = []