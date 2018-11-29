
import socket
import threading
import time


class BroadcastManager:

    def __init__(self, configurationData, continuousBroadcast):
        port = configurationData.GetPort()
        self._message = configurationData.GetMessage()
        self._continuousBroadcast = continuousBroadcast
        self._delay = configurationData.GetInitialDelay()
	
        self._socketAddress = ('255.255.255.255', port)
        self._broadcastSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._broadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


    def StartBroadcastAsync(self):
        broadcastThread = threading.Thread(target=self._startBroadcast)
        broadcastThread.start()
	

    def _startBroadcast(self):
        self._broadcastAfterDelay(self._delay)
        while(self._continuousBroadcast):
            self._broadcastAfterDelay(self._delay)
            
    
    def _broadcastAfterDelay(self, delay):
        time.sleep(delay)

        hostname = socket.gethostname() 
        ipAddress = socket.gethostbyname(hostname)
                    
        message = '<SystemDetails><hostname>' + hostname + '</hostname><ipAddress>' + ipAddress + '</ipAddress><message>' + self._message + '</message></SystemDetails>'
        self._broadcastSocket.sendto(message, self._socketAddress)
        