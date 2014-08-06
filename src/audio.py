# This module will manage the audio stream
# Last modification : Loic then D3Rnatch

#!/usr/bin/env python
import pyaudio
import sys
import time

class audio_core:

	# Callback function (necesary in constructor) returns chunk from stream input.
	def callback(in_data, frame_count, time_info, status):
    	data = self.wf.readframes(frame_count)
    	return (data, pyaudio.paContinue)
	
	# Constructor
	# This method will instanciate a audio manager on the device.
	# If a file_name is defined, the wave file will be streamed in the network (only if the defice is a source)
	# The source argument define if the device is a source (0 or 1) and if it should 
	# The sink argument define if the device is a sink (0 or 1) and if it should play what it can read
	def __init__(self, file_name=""):
		# this constructor inits
		self.p = pyaudio.PyAudio()	  # instanciate the pyaudio module
		if file_name != "" :		  # if wave file given in entry
			self.fileName = file_name
			self.isFromFile = True
			
		elif not file_name :
			self.CHUNK = 1024
			self.FORMAT = pyaudio.paInt16
			self.CHANNELS = 2
			self.RATE = 44100
			self.isFromFile = False
			self.fileName = ""
			if sys.platform == 'darwin':
			self.CHANNELS = 1

	# this function acts has a destructor
	def __stop__(self) :
		#this is the destructor
		self.disable_readMode()
		self.p.terminate()

	# Play the "data" => more like puting data into the pipe
	# @param self, 
	# @param data : chunk to be read
	def Play(self, data):
		stream = self.p.open(format = self.FORMAT,
                channels = self.CHANNELS,
                rate = self.RATE,
                output = True)
		stream.write(data)
		stream.close()

	def enable_readMode(self) :
		if self.isFromFile == True :
			self.wf = wave.open(self.fileName, 'rb')
			self.CHUNK = 1024
			self.FORMAT = p.get_format_from_width(wf.getsampwidth())
			self.CHANNELS = wf.getnchannels()
			self.RATE = wf.getframerate()
			self.isOpened = True

	def disable_readMode(self) :
		if self.isFromFile == True :
			self.wf.close()
			self.isOpened = False
			
	# Get data from the audio source (file if defined, mic otherwise)
	# @param : counter is the chunk's number, 
	# @param : chunk_max : no use
	def Read(self,counter=0,chunk_max=0):
		if self.isFromFile == True and self.isOpened == True:
			data = 'a'
			for i in range(0,counter+1):
				if i != 0 and data != '' :
					data = self.wf.readFrames(self.CHUNK)
				elif data == '' :
					return '-1'
			return data	
		elif self.isOpened == False :
			print "File is not opened, please call : audio.enable_readMode function
			
		else :
			stream = self.p.open(format = self.FORMAT,
                channels = self.CHANNELS,
                rate = self.RATE,
                input=True,
                frames_per_buffer=self.CHUNK)
			data = stream.read(self.CHUNK)
			stream.stop_stream()
			stream.close()
			
			return data




