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

from Listener.BroadcastListener import BroadcastListener

def main():
	broadcastListener = BroadcastListener(12345)
	broadcastListener.StartListenerAsync()
	
	while(True):
		time.sleep(5)

if __name__ == '__main__':
	main()