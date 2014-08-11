# This is a simple example of the network manager 

from random import randint
import select
import signal
import sys

sys.path.insert(0, '../src/')
from audio import *
from network import network_manager

global audio
audio = audio_core()

def data_rec(data):
	print 'Data received : ', data

print 'Select a port'
port = raw_input()

net = network_manager(port, audio.Play, audio.Read)

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