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
	def Connect_to(self, ip_addr):
		try:
			print 'Connect to ', ip_addr
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip_addr, self.port))
			self.clients.append(s)
			print 'Connection OK'
		except Exception, e:
			print 'Exception while connecting to :', ip_addr, '\n\t', e

	# Start the server
	def Start_listenning(self):
		try:
			print 'Start listenning on port ', self.port
			self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.server_socket.bind(('', port))
			self.server.listen(5)
			print 'Listening OK'
		except Exception, e:
			print 'Error while trying to listen :\n\t', e
			

	# Process the network magic (each loop tic)
	def Network_magic(self):
		try:
			inputready, outputready, exceptready = select.select(self.server_socket, [], [])
		except select.error, e:
			print 'FATAL SELECT ERROR !'
			exit()
		except socket.error, e:
			print 'FATAL SOCKET ERROR !'
			exit()

		for s in inputready:
			# New connection
			if s == self.server_socket:
				client, addr = self.server_socket.accept()
				print 'New connection from ', addr
				self.clients.append(client)
			# Incoming data
			else:
				try:
					data = server_socket.recv(1024)
					if data:
						self.proc_func(data)
					else:
						print 'Connection lost !'
						self.clients.remove(s)
				except socket.error, e:
					print 'Error while reading input data !'

	# Send to all clients
	def Send_to_all(self, message):
		for s in self.clients:
			print 'Sending data.'
			s.send(message)

	# Close everything properly
	def Close(self):
		for s in self.clients:
			s.close
			
		self.server_socket.close()


