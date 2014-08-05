# This source code implements the following test :
# sends an audio stream through a local socket.
# by D3Rnatch on 4/08

import socket               # Import socket module

import pyaudio		    # Imports of PyAudio
import wave
import sys

# /////////////////////////////////////////////////
# initialization of PyAudio

print "==Client is setting Audio system.=="

CHUNK = 64 # number of parts made on audio stream
FORMAT = pyaudio.paInt16 # 16 bits format
CHANNELS = 2 # 2 channels : STEREOOOOOO
RATE = 44100 # U No the Stuff called Shanon wtf condition ?
RECORD_SECONDS = 5 # Time of record
WAVE_OUTPUT_FILENAME = "output.wav" # seriously u want something on that ?

if sys.platform == 'darwin':
    CHANNELS = 1

p = pyaudio.PyAudio() # Starting the Audio framework


stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# frames = []

#////////////////////////////////////////////////////////:
# initializing the socket... Connecting to server.

print "==Setting connection to server.=="

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
# host = "172.17.66.208"
port = 12345                # Reserve a port for your service.

s.connect((host, port))	    # Connecting.
# after opening the socket, we read audio input data...

print("* recording")

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    # frames.append(data)
    s.send(data)

# for each frame received it is sent through the socket...

print "Data has been sent to server."

print s.recv(1024)

s.close                     # Close the socket when done
