#This module is in charge of kodo.

import kodo

class NC_manager:

	# Constructor
	# Define a NC manager
	#  - symbols : number of symbols
	#  - symbol_size : symbol size
	def __init__(self, symbols, symbol_size):
		# Construct the encoder
		self.encoder_factory = kodo.full_rlnc_encoder_factory_binary8(symbols, 
									symbol_size)
		self.encoder = self.encoder_factory.build()

		# Construct the decoder
		self.decoder_factory = kodo.full_rlnc_decoder_factory_binary8(symbols,
									symbol_size)
		self.decoder = self.decoder_factory.build()

	# Encode some data
	def Encode(self, data):
		self.encoder.set_symbols(data)

	# Get packets
	def Get_packet(self):
		return (self.encoder.encode())

	# Try to decode some packet
	def Decode(self, packet):
		self.decoder.decode(packet)
		if decoder.is_complete():
			return True
		else:
			return False

	# Get data out
	def Get_data_out(self):
		return decoder.copy_symbols()		
