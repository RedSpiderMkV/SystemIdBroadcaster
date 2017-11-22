
import socket
import threading
import time

class BroadcastManager:
	def __init__(self, configurationData):
		self._port = configurationData.GetPort()
		self._message = configurationData.GetMessage()
	
	def StartBroadcastAsync(self):
		broadcastThread = threading.Thread(target=self._startBroadcast)
		broadcastThread.start()
	
	def _startBroadcast(self):
		while(True):
			socketAddress = ('255.255.255.255', self._port)
			broadcastSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			broadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
			broadcastSocket.sendto(self._message, socketAddress)
			
			time.sleep(5)
