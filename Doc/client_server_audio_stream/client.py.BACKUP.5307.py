#!/usr/bin/env python
import pyaudio
import socket
import sys
import time

# Pyaudio Initialization
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 10240

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

audioInputMode = False # manages the input mode : streaming sound input 

# Socket Initialization

<<<<<<< HEAD
host = '192.168.2.50'
=======
host = '192.168.2.224'
>>>>>>> f72f44d421ad4f573beedc18901759acce918252
#host = socket.gethostname()
port = 12345
size = 1024
s = socket.socket()

# Error management
try:
	s.connect((host,port))
except Exception, e:
<<<<<<< HEAD
	print "An error cured while connecting !\n\t%s\nExit\n", (`e`)
=======
	print 'An error cured while connecting !\n\t', e
	print '\n Exit \n'
>>>>>>> f72f44d421ad4f573beedc18901759acce918252
	exit()

print "Client is connected to : ", host

# Main Functionality
while 15:
    entry = sys.stdin.read(1)
    if entry == "s" :
	audioInputMode = not audioInputMode
	print "Switching mode to : ", audioInputMode

    if audioInputMode == True :
	print "sending mode :"
    	data = stream.read(chunk)
	try:
    		send = s.send(data)
		print 'Sended ', send
	except Exception, e:
		print 'Error while sendig data !\n\t%s\nExit\n', `e`
		exit()

	try:
    		s.recv(size)
	except Exception, e:
		print 'Error while receiving data !\n\t%s\nExit\n', `e`

    if audioInputMode == False :
	print "receiving mode : "
	#inp = s.recv(chunk)
    	#if inp :
	    # treatement here 
	#    print " in mode reading : %s", inp

s.close()
stream.close()
p.terminate()
