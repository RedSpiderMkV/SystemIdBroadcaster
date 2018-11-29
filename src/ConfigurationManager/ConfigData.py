
class ConfigData:
    ''' ConfigData entity - used to provide a model for configuration
        data. '''
		
    def __init__(self, port, message, initialDelay):
        ''' Instantiate a new ConfigData object with the provided
            configuration parameters.
            
            @param: port - integer - the network port.
            @param: message - string - broadcast message. 
            @param: initialDelay - integer - the initial delay in seconds. '''
			
        self._port = port
        self._message = message
        self._initialDelay = initialDelay
        
		
    def GetPort(self):
        ''' Get the port configuration information.
        
            @returns: integer - port setting. '''
			
        return self._port

		
    def GetMessage(self):
        ''' Get the message information.
        
            @returns: string - message setting. '''
			
        return self._message
    

    def GetInitialDelay(self):
        ''' Get the initial delay.
        
            @returns: integer - the initial delay in seconds. '''
            
        return self._initialDelay
