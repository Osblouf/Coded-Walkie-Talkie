# This is a simple example of the network manager 

from network import network_manager
from random import randint
from audio import *
import select
import signal
import sys

global audio = audio_core()

def data_rec(data):
	print 'Data received : ', data

print 'Select a port'
port = raw_input()

net = network_manager(port, audio.Read)

def closing():
	net.Close()

signal.signal(signal.SIGINT, closing)

no_all_ip = True

while no_all_ip:
	print 'select IP to connect to'
	ip = raw_input()
	if ip != '':
		print 'select port'
		port_dest = raw_input()
		net.Connect_to(ip, port_dest)
	else:	
		no_all_ip = False

net.Start_listenning()


while 1:
	net.Network_magic()
	
	#print '==> Send message...'
	#net.Send_to_all('Message !')

net.Close()
