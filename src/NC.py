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
		# Construct the encoder
		self.encoder_factory = kodo.full_rlnc_encoder_factory_binary(symbols, 
									symbol_size)
		self.encoder = self.encoder_factory.build()

		# Construct the decoder
		self.decoder_factory = kodo.full_rlnc_decoder_factory_binary(symbols,
									symbol_size)
		self.decoder = self.decoder_factory.build()

	# Encode some data
	def Encode(self, data):
		self.encoder.set_symbols(data_in)

	# Get packets
	def Get_paket(self):
		return (self.encoder.encode())

	# Try to decode some packet
	def Decode(self, packet):
		self.decoder.decode(packet)
		if decoder.is_complete():
			return True
		else:
			return False

		
