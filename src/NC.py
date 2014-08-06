# This module is in charge of the network coding. It simply uses kodo.

import kodo

class NC_manager:

	# Constructor
	# Define a NC manager
	#  - symbols : number of symbols
	#  - symbol_size : symbol size
	#  - mode : encoding / decoding mode 
	#		- 'normal' : encode and decode the full matrice
	#		- 'on the fly' : encode and decode on the fly
	#		- 'window' : encode and deccode in window mode
	def __init__(self, symbols, symbol_size, mode):

	# Encode some data
	def Encode(self, data):

	# Decode some data
	def Decode(self, data):
