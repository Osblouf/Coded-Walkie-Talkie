# wrapper class for UDP net programming
# by D3Rnatch

import select
import socket
import sys
import signal

class UDPsocket:
	
	
	def __init__ (self,host='127.0.0.1',port='12000') :
		self.UDP_IP = host
		self.UDP_PORT = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
		print "Server >>> UDPSOcket created at ", host, " on ", port

	def stop(self) :
		self.sock.close()

	def setListener(self) :
		try :
			self.sock.bind((self.UDP_IP, self.UDP_PORT))
        	except Exception, e :
          		print 'Server Error >>> Error on Binding : ', e

	def read(self,size) :
		return self.recv(size)
	
	def write(self,data) :
		sock.sendto(data, (self.UDP_IP, self.UDP_PORT))
	
