def a(s=[i+2 for i in range(10)]):
	print hex(id(s))

a()
a([])