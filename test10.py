def y():
	yield 1
	yield 2
	yield 3
	yield 4

it = iter(y());
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))


for i in y():
	print(i)