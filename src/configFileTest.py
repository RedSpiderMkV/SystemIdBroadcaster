
from ConfigurationManager.ConfigurationManager import ConfigurationManager

def main():
	fileManager = ConfigurationManager('broadcast.config')
	[port, message] = fileManager.GetConfigurationData()
	
	print port
	print message

if __name__ == '__main__':
	main()
