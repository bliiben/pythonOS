# a={"coucou":6,'tr':2}
# def ok(l):

# 	return l==2
# b=dict(filter(ok ,a.items() ))
# for i in a.keys():
# 	print(i)


# a= "mary had a little little lamb"
# for c in a[11:18] :
# 	print c,
# 	if "little" in c: print c 

# def c():
# 	if a==2:
# 		print "truc"

# c()

# def fun1(x,y,z) :
# 	if x == 1 :
# 		return fun2(y, y=z)
# 	elif x == 2 :
# 		return x + y + z
# 	elif x == 3 :
# 		return fun2(y=9,z=x+y)
# 	else :
# 		return 17

# def fun2(x=7,y=9,z=11) :
# 	if x == 2 :
# 	   return x+y+z   
# 	elif x == 7 :
# 	   return x*y*z
# 	else :
# 	   return 42 

#print(fun1(1,2,3))

# class CoordsA(object):
# 	__slots__=["x","y","z"]
# 	w = 1

# class CoordsB(CoordsA):
# 	__slots__=["w","z"]
# 	pass

# a = CoordsA()
# b = CoordsB()

# a.x=40


# data = [1,2,3,4,5,6]

# def f1(x):
#     return 3 * x

# def f2(x):
#     try:
#         return x > 3
#     except:
#         return 0 

# result = map(f1, filter(f2, data))
# print ([3*i for i in data(i) if i > 3])
# print(map(lambda r: r * 3, filter(lambda f: f>3 or 0, data)))
# print(map(lambda r: r * 3, filter(f2, data)))

# vector= [[1,2],[3,4],[5,6],[7,8],[9,10]]
# print( [x for y in vector for x in y if x % 2 == 0 ])

# for n in range(2,10) :
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else:
#         print n 


# class k:
# 	def __init__(self):
# 		self.__foo = 10    
# 	def methodX(self):
# 		self.__methodY()
# 		print self.__foo
# 	def __methodY(self):
# 		self.__foo += 1
# o = k() 
# o.methodX()
# #o.__methodY()
# #o.__foo
# o._k__methodY()
# o.__init__()
# def test(x) :
#     print x
#     if x % 3 == 0 : return test(x/3)
#     if x % 2 == 1 : return x
#     return test(2*x+1)
# def test(x) :
# 	print x
# 	if x % 3 == 0 : return test(x/3)
# 	if x % 2 == 1 : return x
# 	return test(2*x+1)
# print (test(100))

# x = [1,2,3]
# y = (1,2,3) 
# y=x

# IPlist = ['209.85.238.4','216.239.51.98','64.233.173.198','64.3.17.208','64.233.173.238']

# tmp = [list(map(str, ip.split("."))) for ip in IPlist]
# tmp.sort()
# IPlist = [".".join(map(str, address)) for address in tmp]
# IPlist.sort(key=lambda address: map(str, address.split('.')))

# IPlist = ['209.85.238.4','216.239.51.98','64.233.173.198','64.3.17.208','64.233.173.238']
# IPlist.sort(key=lambda address: map(int, address.split('.')))


# IPlist = ['209.85.238.4','216.239.51.98','64.233.173.198','64.3.17.208','64.233.173.238']
# for address in range(len(IPlist)):
# 	IPlist[address] = '%3s.%3s.%3s.%3s' % tuple(IPlist[address].split('.'))
# 	IPlist.sort(reversed=False)


# IPlist = ['209.85.238.4','216.239.51.98','64.233.173.198','64.3.17.208','64.233.173.238']
# for address in range(len(IPlist)):
# 	IPlist[address] = IPlist[address].replace(' ', '')

# tmp = [tuple(map(int, ip.split("."))) for ip in IPlist]
# tmp.sort(reversed=False)
# IPlist = [".".join(map(str, address)) for address in tmp] 

class A(object):
	def __init__(self):
		print "%d" % 1
		super(A,self).__init__()
		print "<%d>" % 1

class B(object):
	def __init__(self):
		print "%d" % 2
		super(B,self).__init__()
		print "<%d>" % 2

class C(A,B):
	def __init__(self):
		print "%d" % 3
		super(C,self).__init__()
		print "<%d>" % 3


print(sum([n * n for n in range(1, 10)]) == sum(n * n for n in xrange(1, 10)))
print(([n * n for n in range(1, 10)]) == sum(n * n for n in xrange(1, 10)))
print([n * n for n in range(10, 11)] == sum(n * n for n in xrange(10, 11)))
print(([n + n for n in range(1, 10)]) == (n * 2 for n in xrange(1, 10)))
print(sum([1 * n for n in range(0, 5)]) == sum(n for n in xrange(0, 5)))