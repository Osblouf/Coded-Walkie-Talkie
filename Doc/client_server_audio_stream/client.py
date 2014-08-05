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

# Socket Initialization
host = socket.gethostname()
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

# Main Functionality
while 1:
    data = stream.read(chunk)
    s.send(data)
    s.recv(size)

s.close()
stream.close()
p.terminate()
