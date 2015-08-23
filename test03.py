try:
	r = input("give me something")

	r=int(r)

	if (isinstance(r,int)):
		raise ValueError("incorrect data feeded")

except Exception as e:
	print("2",e)
else:
	print("great r is ",r)
finally:
	print("I'm done with this shit")
