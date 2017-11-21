
class ConfigData:
	''' ConfigData entity - used to provide a model for configuration
		data. '''
		
	def __init__(self, port, message):
		''' Instantiate a new ConfigData object with the provided
			configuration parameters.
			
			@param: port - integer - the network port.
			@param: message - string - broadcast message. '''
			
		self._port = port
		self._message = message
		
	def GetPort(self):
		''' Get the port configuration information.
		
			@returns: integer - port setting. '''
			
		return self._port
		
	def GetMessage(self):
		''' Get the message information.
		
			@returns: string - message setting. '''
			
		return self._message
