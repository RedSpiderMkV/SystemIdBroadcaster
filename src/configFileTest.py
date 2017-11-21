
from ConfigurationManager.ConfigurationManager import ConfigurationManager

def main():
	fileManager = ConfigurationManager('broadcast.config')
	configurationData = fileManager.GetConfigurationData()
	
	print configurationData.GetPort()
	print configurationData.GetMessage()

if __name__ == '__main__':
	main()
