#!/usr/bin/python

import time

from Broadcaster.BroadcastManager import BroadcastManager
from ConfigurationManager.ConfigurationManager import ConfigurationManager


def main():
	configurationManager = ConfigurationManager('broadcast.config')
	configurationData = configurationManager.GetConfigurationData()
	
	continuousBroadcast = False
	broadcastManager = BroadcastManager(configurationData, continuousBroadcast)
	broadcastManager.StartBroadcastAsync()
	
	while(continuousBroadcast):
		time.sleep(60*5)


if __name__ == '__main__':
	main()
