class Papa:
	"""docstring for Papa"""
	def __init__(self, age):
		self.age = age

class Enfant(Papa):
	"""docstring for Enfant"""
	def __init__(self, nom):
		super(Enfant, self).__init__(1)
		self.nom = nom

	def __str__(self):
		return self.nom+" a "+str(self.age)+" an"

e= Enfant("Joe")
print(e)