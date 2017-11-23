#!/usr/bin/python

import time

from Broadcaster.BroadcastManager import BroadcastManager
from ConfigurationManager.ConfigurationManager import ConfigurationManager

def main():
	configurationManager = ConfigurationManager('broadcast.config')
	configurationData = configurationManager.GetConfigurationData()
	
	broadcastManager = BroadcastManager(configurationData)
	broadcastManager.StartBroadcastAsync()
	
	while(True):
		time.sleep(60*5)

if __name__ == '__main__':
	main()
