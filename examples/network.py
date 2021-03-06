# Network module
# This module will be in charge of the network 
# Last modification : Loic 

import select
import socket
import sys
import signal

class network_manager:
	# Class arguments :
	#	- self.port		: port used
	#	- self.proc_func	: function used to process data received
	#	- self.clients		: socket list of connections
	#	- self.server_socket	: listening server socket
	# Constructeur
	def __init__(self, port, process_function):
		self.port = port
		self.proc_func = process_function
		self.clients = []

	# Connect to a server
	def Connect_to(self, ip_addr, port):
		try:
			print 'Connect to ', ip_addr
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip_addr, int(port)))
			self.clients.append(s)
			print 'Connected'
		except Exception, e:
			print 'Exception while connecting to :', ip_addr, '\n\t', e

	# Start the server
	def Start_listenning(self):
		try:
			print 'Start listenning on port ', self.port
			self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.server_socket.bind(('', int(self.port)))
			self.server_socket.listen(5)
			print 'Listening OK'
		except Exception, e:
			print 'Error while trying to listen :\n\t', e
			

	# Process the network magic (each loop tic)
	def Network_magic(self):
		try:
			#print '[Debug] is ready ?'
			inputs = list()
			del inputs[:]
			inputs.extend(self.clients)
			inputs.append(self.server_socket)
			inputs.append(sys.stdin)
			inputready, outputready, exceptready = select.select(inputs, [], [], 0)
		except select.error, e:
			print 'FATAL SELECT ERROR !'
			exit()
		except socket.error, e:
			print 'FATAL SOCKET ERROR !'
			exit()
		except Exception, e:
			print 'Error with select :\n\t', e
			exit()


		for s in inputready:
			#print '[Debug] Something is ready !'
			# New connection
			
			if s == self.server_socket:
				client, addr = self.server_socket.accept()
				print 'New connection from ', addr
				self.clients.append(client)
			elif s == sys.stdin:
				text = sys.stdin.readline()
				self.Send_to_all(text)
			# Incoming data
			else:
				try:
					data = s.recv(1024)
					if data:
						self.proc_func(data)
					else:
						print 'Connection lost ! from ', s.getpeername()
						self.clients.remove(s)
				except socket.error, e:
					print 'Error while reading input data !'

	# Send to all clients
	def Send_to_all(self, message):
		for s in self.clients:
			print 'Sending data.'
			try:
				s.send(message)
			except Exception, e:
				print 'Error while sendig data : \n\t', e

	# Close everything properly
	def Close(self):
		for s in self.clients:
			s.close
			
		self.server_socket.close()


