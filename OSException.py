class OsException(Exception):
	"""Error thrown by our OS need to implement this"""
	def __init__(self, message, error={}):
		super(OsException, self).__init__(message)
		self.message = message
		self.error = error
		self.type="BaseException"

class InvalidOperation(OsException):
	"""Operation is not valid"""
	def __init__(self, message, error={}):
		super(InvalidOperation, self).__init__(message,error)
		self.type="InvalidOperation"