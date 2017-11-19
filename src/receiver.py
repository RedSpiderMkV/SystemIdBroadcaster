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

import socket

def StartListener(port):
    listenerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listenerSocket.bind(('', port))

    message = listenerSocket.recvfrom(1024)
    print message[0]