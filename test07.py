class TableauNoir:
	"""docstring for TableauNoir"""
	def __init__(self):
		self.surface="";

	def ecrire(self,message):
		self.surface=self.surface+"\n"+message

	def lire(self):
		print(self.surface)

	def effacer(self):
		self.surface=""

tab=TableauNoir();
tab.lire()
tab.ecrire("Coucou les debiles")
tab.ecrire("vous etes toujours la")
tab.lire()
tab.effacer()
tab.lire()
