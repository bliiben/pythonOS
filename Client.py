import threading 
import Os

class Client(threading.Thread):
	"""docstring for Client"""

	def __init__(self,name,os):
		super(Client, self).__init__()
		self.name=name
		self.os=os
		self.newProgram = threading.Event()
		self.newProgram.set()

	def run(self):
		#lance un programme
		while self.newProgram.wait():
			self.os.addProgram("r0:1,r2:4+r0,r1:r2-r0",self)
			self.newProgram.clear()

	def notice(self,value):
		print("result",value)
		#run another program


	def isRunning(self,value):
		print ( self.name +" has " + ("started running" if value \
			else "stopped running"))


Client("s",Os.Os())