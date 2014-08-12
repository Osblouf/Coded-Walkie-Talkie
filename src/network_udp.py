# Network UDP client/relay/server manager class
# by D3Rnatch on 11/08

import select
import socket
import sys
import signal

from UDPsocket import UDPsocket

class UDP_network_manager:

	def __init__(self, servAddr, destAddr, servport, send_function ,read_function):
		self.broadcast = destAddr
		self.server = servAddr
		self.port = servport
		self.sendFunc = send_function
		self.readFunc = read_function
		print " Server >>> Server created on port : ", self.port, ", brdCAST is :", self.broadcast
		print " Server >>> Server is :", self.server

	def Start_listenning(self) :
		try :
			print " Server >>> listenning on port :", self.port
			self.destSock = UDPsocket(self.broadcast,self.port)
			self.server_socket = UDPsocket(self.server, self.port)
			self.server_socket.setListener() # here this socket is binded on self.port

		except Exception, e :
			print "Server Fatal Error >>>", e
			exit()


	def Network_magic(self) :
		try:
			#print '[Debug] is ready ?'
			#inputs = list()
			#del inputs[:]
			#inputs.append(self.server_socket) # listener socket is insert into stack
			#inputs.append(sys.stdin)  # user input also
			inputready, outputready, exceptready = select.select([self.server_socket.sock, sys.stdin,], [], [], 0) 
		except select.error, e:
			print 'FATAL SELECT ERROR !'
			exit()
		except socket.error, e:
			print 'FATAL SOCKET ERROR !'
			exit()
		except Exception, e:
			print 'Error with select :\n\t', e
			exit()

		# for inputsready stuff...
		for s in inputready:
			#print '[Debug] Something is ready !'
			# New connection
			if s == sys.stdin:
				text = sys.stdin.readline()
				
				self.Send_to_all(self.sendFunc())
			# Incoming data
			else:
				try:
					data, addr = self.server_socket.read(1024)
					#print "Server >>> Data received from : ", addr
					if data:
						self.readFunc(data)
					else:
						print "Server Error >>> Data read is empty !"
				except socket.error, e:
					print "Server Error >>> Socket error on reading data : ", e

	def Send_to_all(self, data) :
		try :
			self.destSock.write(data)
		except Exception, e :
			print "Server Error >>>",e



