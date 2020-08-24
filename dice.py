from random import randint

class Dice:
	"""A class representing a single Die."""
	def __init__(self, num_sides = 6):
		"""Assume a six-sided Die"""
		self.num_sides = num_sides


	def roll(self):
		"""Return a number between 1 and number of sides"""
		return randint (1,self.num_sides)
		

