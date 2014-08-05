# Network module
# This module will be in charge of the network 
# Last modification : Loic 

class network_manager:
	#This module manage the network in the project coded walkie talkie.

	#This module's fields are listed below:
	# - n_mode : mode of connection used to connect the device


	#Start with initiate the mode you want :
	#- 'normal' will use the normal use of network like sockets, one route, etc

	
	#start the network module with this method
	#Start with initiate the mode you want :
	#- 'normal' will use the normal use of network like sockets, one route, etc
	def __init__(self, mode=""):
		if mode == 'normal':
			print 'Start the network in normal mode sockets, route and shit...'
			self.n_mode = mode

		else:
			print 'You should specify a mode to run the network manager !'
			self.n_mode = 'none'


	# Read from the network network return the new data
	def Get_data(self):

	# send something on the network
	def Send(self, data):

	# Process the magic of network coding
	def Process_magic(self):
