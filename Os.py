import OSException
import CPU
from collections import deque
import threading 

class Os(threading.Thread):
	"""docstring for OS"""
	def __init__(self):
		threading.Thread.__init__(self)
		self.programs = deque()
		self.lock = threading.RLock()
		self.isUpdates = threading.Event()

	def addProgram(self,program,client):
		with self.lock:
			self.programs.appendleft({"programString":program,"client":client})
		self.isUpdates.set()

	def run(self):
		print("Waiting....")
		while self.isUpdates.wait():
			print("Something to process !")
			programToRun=None
			with self.lock:
				if len (self.programs) != 0:
					print("number of programs",len (self.programs))
					programToRun = self.programs.pop()

			if programToRun != None:
				#programToRun["client"].running=True
				#Has the program already been started once ?
				if "program" not in programToRun.keys():
					programToRun.update(CPU.startProgram(programToRun["programString"]))
				else:
					programToRun.update(CPU.execute(programToRun["program"],programToRun["memory"],programToRun["state"]))

				#programToRun["client"].running=False
				with self.lock:
					if len(programToRun["program"])==programToRun["state"]:
						print("program finished", "memory is ",hex(id(programToRun["memory"])), "of" ,programToRun["programString"])
					else:
						self.programs.appendleft(programToRun)
			else :
				self.isUpdates.clear()
				print ("Waiting for new programs to process...")

if __name__ == '__main__':
	os=Os()
	os.start()
	os.addProgram("r0:1,r2:4+r0,r1:r2-r0",{"running":False})
	os.addProgram("r0:1,r0:r0+r0,r0:r0+r0,r0:r0+r0,r0:r0+r0",{"running":False})
