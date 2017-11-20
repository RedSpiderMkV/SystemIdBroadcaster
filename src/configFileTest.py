
from ConfigurationManager.ConfigurationManager import ConfigurationManager

def main():
	fileManager = ConfigurationManager('testFile.xml')
	fileManager.ReadConfiguration()

if __name__ == '__main__':
	main()
