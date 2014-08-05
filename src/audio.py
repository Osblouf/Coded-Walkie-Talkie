# This module will manage the audio stream
# Last modification : Loic

class audio_core:

	# Constructor
	# This method will instanciate a audio manager on the device.
	# If a file_name is defined, the wave file will be streamed in the network (only if the defice is a source)
	# The source argument define if the device is a source (0 or 1) and if it should 
	# The sink argument define if the device is a sink (0 or 1) and if it should play what it can read
	def __init__(self, file_name=""):

	# Play the "data" => more like puting data into the pipe
	def Play(self, data):

	# Get data from the audio source (file if defined, mic otherwise)
	def Read(self):
