
import socket
import threading
import time

class BroadcastListener:
	def __init__(self, port):
		self._port = port
		
	def StartListenerAsync(self):
		listenerThread = threading.Thread(target=self._startListener)
		listenerThread.start()
	
	def _startListener(self):
		listenerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		listenerSocket.bind(('', self._port))

		while(True):
			receivedData = listenerSocket.recvfrom(1024)
			sender = receivedData[1]
			
			ipAddress = sender[0]
			port = sender[1]
			message = receivedData[0]
			
			print ipAddress + ':', message
			
			time.sleep(1)
