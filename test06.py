d={"benjamin":4,"antoine":10}
for i,b in d.items():
	print (" {} = {}".format(i,b))

def abc(*values):
	for i in values:
		print(i)

l=["coucou","truc",['s','v']]
abc(*l)