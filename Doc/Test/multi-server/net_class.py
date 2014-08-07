# Manage the network

# Last modification : Loic
import threading
import socket

class Net_manager:

	# List of all client
	global clients
	global receive_func
	global clients_threads
	global run
	global server_thread

	# Constructor :
	def __init__(self, port, received_function):
		self.port = port
		Net_manager.receive_func = received_function
		Net_manager.run = True
		Net_manager.clients = list()
		Net_manager.clients_threads = list()
		
	# Connect to an other device
	def Connect_to(self, ip_addr):
		s = socket.socket()
		try:
			print 'Try connecting to : ', ip_addr
			s.connect((ip_addr, self.port))
			Net_manager.clients.append(s)
			th = threading.Thread(None, 
					Net_manager.Client_thread_func,
					None, 
					(s,), 
					None)
			th.daemon = True
			th.start()
			Net_Manager.clients_threads.append(th)
			print 'Connection OK.'
		except Exception, e:
			print "Error while connection to ", ip_addr, ".\n\t", e		

	# Start the server to listen all incoming connections
	def Start_listening(self):
		print 'Start listening...'
		Net_manager.server_thread = threading.Thread(None, Net_manager.Listening_thread_func, None, (self.port,), None)
		Net_manager.server_thread.daemon = True
		Net_manager.server_thread.start()
		print 'Listening ok.'

	# Send to all
	def Send_to_all(self, data):
		print 'Send to all...'
		for sock in Net_manager.clients:
			print '.'
			sock.send(data)
		print 'Send OK.'

	# Listening thread function
	@staticmethod
	def Listening_thread_func(port):
		s = socket.socket()
		s.bind((socket.gethostname(), port))
		s.listen(5)

		while Net_manager.run:
			client, address = s.accept()
			print 'Incoming connection from : ', address
			Net_manager.clients.append(client)
			th = threading.Thread(None, 
					Net_manager.Client_thread_func,
					None,
					(client,),
					None)
			th.daemon = True
			th.start()
			Net_manager.clients_threads.append(th)
			print 'Connection OK'


	# Client thread function
	@staticmethod
	def Client_thread_func(sock):
		while Net_manager.run:
			data = sock.recv()
			print '(data received)'
			Net_manager.receive_func(data)
		
	# Close all threads and sockets
	def Close(self):
		print 'Close everything...'
		Net_manager.run = False
		if len(Net_manager.clients) != 0:
			for sock in Net_manager.clients:
				sock.close()
		
		#if len(Net_manager.clients_threads) != 0:
		#	for th in Net_manager.clients_threads:
		#		th._stop()
		#Net_manager.server_thread._stop()

		print 'Closing OK.'

