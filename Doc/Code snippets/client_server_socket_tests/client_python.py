import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
#host = "192.168.43.163"
port = 50000                # Reserve a port for your service.

try:
	s.connect((host, port))
except Exception, e:
	print 'Something went wrong while connecting ! \n\t%s' % `e`
	exit()

print s.recv(1024)
s.close                     # Close the socket when done
