
import os
from ConfigData import ConfigData

class ConfigurationManager:
	''' ConfigurationManager class - extracts configuration data from
		the config file provided. Config file is expected to be an XML
		file following the required schema.
	'''
	
	def __init__(self, filePath):
		''' Initialise a new ConfigurationManager object to parse
			system broadcast ID configuration data.
			
			@param filePath: string - path to configuration file.
			@exception: FileNotFoundException - thrown if provided file
				path does not exist.
		'''
		
		if not os.path.isfile(filePath):
			raise(IOError("File does not exist"))
			
		self._configFile = filePath
	
	def GetConfigurationData(self):
		''' Get configuration data from file.
		
			@returns: ConfigData - Configuration data wrapped within a
				ConfigData object. '''
				
		with open(self._configFile, 'r') as f:
			content = f.read()
			
		broadcastData = content.split('\n')
		portData = broadcastData[0]
		messageData = broadcastData[1]
		initialDelay = broadcastData[2]
		
		port = int(self._getCleanedData(portData))
		message = self._getCleanedData(messageData)
		delay = int(self._getCleanedData(initialDelay))
		
		return ConfigData(port, message, delay)

	def _getCleanedData(self, data):
		return data.split(':')[1].lstrip(' ')
