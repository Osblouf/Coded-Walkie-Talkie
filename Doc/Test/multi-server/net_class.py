# Manage the network

# Last modification : Loic
import threading
import socket

class Net_manage:

	# List of all client
	clients = []
	server_thread

	# Constructor :
	def __init__(self, port):
		self.port = port
		
	# Connect to an other device
	def Connect_to(self, ip_addr):
		s = socket.socket()
		try:
			s.connect((ip_addr, self.port))
			clients.append(s)
		except Exception, e:
			print "Error while connection to ", ip_addr, ".\n\t", e		

	# Start the server to listen all incoming connections
	def Start_listening(self):
		server_thread = threading.Thread(None, Thread_func, None, None, None)

	# Send to all
	def Send_to_all(self, data):
	
	# Thread function
	@staticmethod
	def Thread_func():

	# Close all threads
	def Close(self):

