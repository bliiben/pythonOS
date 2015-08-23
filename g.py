WIDTH = 10
HEIGHT= 10
#
# .___.
# |   |
# .___.
#


class Screen():
	"""docstring for Screen"""
	def __init__(self,lst):
		self.list=lst

	def display(self):
		i=0
		string=string1=string2=string3=string4=""
		while i<HEIGHT:
			j=0
			while j<WIDTH:
				string1+= '.___' if (self.list[i][j] & 1) else '.   '
				string2+= '|   ' if (self.list[i][j] & 2) else '    '
				string3+= '|' if (self.list[i][j] & 4) else ' '
				string4+= '.___' if (self.list[i][j] & 3) else '.   '
				j+=1
			string += string1+"\n"+string2+string3+"\n"+string4+"\n"
			string1=string2=string3=string4=""
			i+=1
		print(string)

class Game():
	"""docstring for Game"""
	def __init__(self):
		self.l=[ [ 0 for i in range(WIDTH) ] for i in range(HEIGHT)]
		#self.l[2][2]=0b1111
		self.s=Screen(self.l)
		self.s.display()


g=Game()