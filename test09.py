class Ob:
	"""docstring for ob"""
	def __init__(self):
		self.truc=4


try:
	raise Ob()
except Ob as e:
	raise e