
import socket
import threading
import time

class BroadcastListener:
	def __init__(self, port):
		self._port = port
		
	def StartListenerAsync(self):
		self._haltFlag = False
		self._listenerThread = threading.Thread(target=self._startListener)
		self._listenerThread.start()
		
	def StopListener(self):
		self._haltFlag = True
		
		socketAddress = ('255.255.255.255', self._port)
		broadcastSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		broadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)		
		broadcastSocket.sendto('end', socketAddress)
	
	def _startListener(self):
		listenerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		listenerSocket.bind(('', self._port))

		while not self._haltFlag:
			receivedData = listenerSocket.recvfrom(1024)
			sender = receivedData[1]
			
			ipAddress = sender[0]
			port = sender[1]
			message = receivedData[0]
			
			print ipAddress + ':', message
			

