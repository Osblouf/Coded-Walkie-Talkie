#this module is in charge of kodo.

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

		# Construct the decoder
		self.decoder_factory = kodo.full_rlnc_decoder_factory_binary8(symbols,
									symbol_size)

	# Encode some data
	def Encode(self, data):
		self.encoder = self.encoder_factory.build()
		self.encoder.set_symbols(bytes(data))

	# Create new encoder 
	def New_decoder(self)
		self.decoder = self.decoder_factory.build()

	# Get packets
	def Get_packet(self):
		return (self.encoder.encode())

	# Try to decode some packet
	def Decode(self, packet):
		self.decoder.decode(packet)
		if self.decoder.is_complete():
			return True
		else:
			return False

	# Get data out
	def Get_data_out(self):
		data = self.decoder.copy_symbols()		
		return data
