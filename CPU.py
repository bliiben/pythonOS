import OSException
		
def execute(program, memory, state=0,numberOfOperation=1):
	print (program,state,memory)
	maxOp = state + numberOfOperation
	while state < len(program) and state < maxOp:
		#type of operation
		if(program[state][0]=='r'):
			print("operation "+str(state)+" is assign")
			doAssign(program[state],memory)
		elif(program[state][0]=='j'):
			print("operation "+str(state)+" is jump")
		else:
			raise InvalidOperation("Program is not valid, error at op: "+str(state))
		
		state+=1

	return {"program":program,"memory":memory,"state":state}

def doAssign(operation,memory):
	endRegister,op =operation.split(':')
	endRegister=int(endRegister[1])
	print("Operation executed", "register_"+str(endRegister), "get" ,op)
	# is it an assign or an op ?
	if('+' in op):
		print("is a +")
		av,ap = op.split('+')
		memory[endRegister]=getValROC(av,memory) + getValROC(ap,memory)

	elif('-' in op):
		print("is a -")
		av,ap = op.split('-')
		memory[endRegister]=getValROC(av,memory) - getValROC(ap,memory)
	else:
		memory[endRegister]=getValROC(op,memory)

	print(memory)

def getValROC(string,memory):
	r=getRegOrC(string)
	if(r[0]=='r'):
		return memory[r[1]]
	else:
		return r[1]

def getRegOrC(string):
	return ( ('r' if string[0] == 'r' else 'c'), \
		int(string[1] if string[0] == 'r' else string) )

def startProgram(programString,numberOfOperation=1):
	memory=[0 for i in xrange(10)]
	return execute(programString.split(','),memory,numberOfOperation=numberOfOperation)

def main():
	startProgram("r0:1,r2:4+r0,r1:r2-r0",1)

if __name__ == '__main__':
	main()