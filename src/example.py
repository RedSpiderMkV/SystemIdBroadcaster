#!/usr/bin/python

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nikeah
#
# Created:     19/11/2017
# Copyright:   (c) Nikeah 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time

from ConfigurationManager.ConfigurationManager import ConfigurationManager
from Broadcaster.BroadcastManager import BroadcastManager
from Listener.BroadcastListener import BroadcastListener

def main():
	configurationManager = ConfigurationManager('broadcast.config')
	configurationData = configurationManager.GetConfigurationData()
	
	broadcastManager = BroadcastManager(configurationData)
	broadcastListener = BroadcastListener(configurationData)
	
	broadcastManager.StartBroadcastAsync()
	broadcastListener.StartListenerAsync()
	
	while(True):
		time.sleep(5)

if __name__ == '__main__':
	main()
