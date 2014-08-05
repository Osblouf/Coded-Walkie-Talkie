import socket               # Import socket module
import pyaudio
import wave
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

if sys.platform == 'darwin':
    CHANNELS = 1

p = pyaudio.PyAudio()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
#host = "172.17.66.208"
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

# ==========================================
# Setting up Audio system
# ==========================================

frames = []

# ==========================================
# Starting the Server
# ==========================================
e = True
s.listen(5)                 # Now wait for client connection.
while e == True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   print "Waiting the chunks :   
   # we read the data...   
   data = s.recv(1024)
   if not data : e = False
   elif data == 'ACK' :
     	e = False
   else :
	frames.append(data)

# Polite Stuff
c.send('Thank you for connecting')



c.close()                # Close the connection

