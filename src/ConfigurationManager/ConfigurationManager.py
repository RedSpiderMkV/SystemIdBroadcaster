
import os
from xml.dom import minidom

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
	
	def ReadConfiguration(self):
		from xml.dom import minidom
		xmldoc = minidom.parse(self._configFile)
		port = xmldoc.getElementsByTagName('Port')[0].data
		message = xmldoc.getElementsByTagName('Message')[0].firstchild.data
		
		print port, message
		
			
		content = None
		with open(self._configFile, 'r') as f:
			content = f.read()
			
		print(content)
