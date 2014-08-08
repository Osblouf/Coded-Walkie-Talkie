# This module will manage the audio stream
# Last modification : D3Rnatch on 7/08 at 10:24
# TO DO List : Debug on file reading
# Notes : --
#!/usr/bin/env python
import pyaudio
import time
import wave
import sys

class audio_core:

	# audio_core parameters 

	# Constructor
	# This method will instanciate a audio manager on the device.
	# If a file_name is defined, the wave file will be streamed in the network (only if the defice is a source)
	# The source argument define if the device is a source (0 or 1) and if it should 
	# The sink argument define if the device is a sink (0 or 1) and if it should play what it can read
	def __init__(self, file_name=""):
		print "Client >>> Starting up Audio Core..."
		self.frames_input = []
		self.frames_output = []
	
		# this constructor inits
		self.p = pyaudio.PyAudio()	  # instanciate the pyaudio module
		self.isContinuousPlay = False
		self.isContinuousReading = False
		self.firstPlay = True		

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
			#if sys.platform == 'darwin':
			#	self.CHANNELS = 1
		else :
			print "audio_core.__init__ : this is debug at starting"
		print "Client >>> Audio Core set up properly..."
		
	# this function acts has a destructor
	# stops every running stuff
	def stop_audioCore(self) :
		#this is the destructor
		try :
			self.disable_readMode()
			self.disable_continuousPlay()
			self.p.terminate()
		except Exception, e:
			print e
			exit()

	# Play the "data" => more like puting data into the pipe
	# @param self, 
	# @param data : chunk to be read
	# Note : this function restarts the output for every packet it plays... 
	# to outdraw this please use : enableContinuousPlay function
	# before calling the play function
	def Play(self, data):
		try :
			#if self.isContinuousPlay != True :
			#	print " is not continuously playin' "
			#	self.stream = self.p.open(format = self.FORMAT,
	                #			     channels = self.CHANNELS,
	                #			     rate = self.RATE,
	                #			     output = True)
			#	self.stream.write(data)
			#	self.frames_output.append(data)
			#	self.stream.close()
			if self.firstPlay == True :
				self.stream = self.p.open(format = self.FORMAT,
	                			     channels = self.CHANNELS,
	                			     rate = self.RATE,
	                			     output = True)
				self.firstPlay = False
			else :
				# print " is continuously playin' "
				self.stream.write(data)
				self.frames_output.append(data)
		except Exception, e :
			print e

	# Get data from the audio source (file if defined, mic otherwise)
	# Note : please call enable_readMode before calling the read function in readFile mode
	# Note 2 : you can also active the continuous reading mode in record Mode by calling :
	#			the enable_continuousReading function. 
	# Note 3 : Care to not call enable_readMode and enable_continuousReading at the same time !
	#			(functions not independent)
	# @param : counter is the chunk's number, 
	# @param : chunk_max : no use
	# /!\ @return : the chunk of size self.chunk or -1 when EOF reached.
	def Read(self,counter=0,chunk_max=0):
		try :
			if self.isFromFile == True and self.isOpened == True:
				data = 'a'
				for i in range(0,counter+1):
					if i != 0 and data != '' :
						data = self.wf.readFrames(self.CHUNK)
					elif data == '' :
						return '-1'
				return data	
			if self.isFromFile == True and self.isOpened == False :
				print "File is not opened, please call : audio_core.enable_readMode function."
				print "values are : ", self.isFromFile	
			else :
				if self.isContinuousReading == False :
					self.stream = self.p.open(format = self.FORMAT,
            	    	channels = self.CHANNELS,
            	    	rate = self.RATE,
            	    	input=True,
            	    	frames_per_buffer=self.CHUNK)
				data = self.stream.read(self.CHUNK)
				self.frames_input.append(data)
				if self.isContinuousReading == False :
					self.stream.stop_stream()
					self.stream.close()
			
				return data
		except Exception, e :
			print e

	# switch_readRecordMode : permits to either read the file sent in input at beginning nor read input device.
	#	/!\ if no input file was specified : the value does not change and record mode will stay.
	# @return : returns the new value of isFromFile (True/False)
	def switch_readRecordMode(self) :
		self.isFromFile = not self.isFromFile
		if self.isFromFile == False :
			self.CHUNK = 1024
			self.FORMAT = pyaudio.paInt16
			self.CHANNELS = 2
			self.RATE = 44100
			self.isFromFile = False
			self.fileName = ""
			if sys.platform == 'darwin':
				self.CHANNELS = 1
		else :
			if self.fileName == "" :
				self.isFromFile = not self.isFromFile
		
		return self.isFromFile
	
	def createWaveFile(self,fileName, frames) :
		self.wf = wave.open(fileName, 'wb')
		self.wf.setnchannels(self.CHANNELS)
		self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
		self.wf.setframerate(self.RATE)
		self.wf.writeframes(b''.join(frames))
		self.wf.close()
	
	# createWaveFileInputFrames : creates a wave file from read frames read.
	# for input tests
	def createWaveFileInputFrames(self) :
		fileName = "input_test_wave.wav"
		self.wf = wave.open(fileName, 'wb')
		self.wf.setnchannels(self.CHANNELS)
		self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
		self.wf.setframerate(self.RATE)
		self.wf.writeframes(b''.join(self.frames_input))
		self.wf.close()
	
	# createWaveFileOutputFrames : creates a wave file from read frames played.
	# for output tests
	def createWaveFileOutputFrames(self) :
		fileName = "output_test_wave.wav"
		self.wf = wave.open(fileName, 'wb')
		self.wf.setnchannels(self.CHANNELS)
		self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
		self.wf.setframerate(self.RATE)
		self.wf.writeframes(b''.join(self.frames_output))
		self.wf.close()
		

	# enable_continuousPlay : enables the script to send chunks to the play function without  
	# 			restarting the device.
	def enable_continuousPlay(self) :
		self.isContinuousPlay = True
		self.stream = self.p.open(format = self.FORMAT,
                channels = self.CHANNELS,
                rate = self.RATE,
                output = True)

	# disable_continuousPlay : disables the continuous play system.
	def disable_continuousPlay(self) :
		self.isContinuousPlay = False
		self.stream.close()

	# enable_readMode : activate the readMode by opening the wave file and sets environment values
	def enable_readMode(self) :
		if self.isFromFile == True :
			self.wf = wave.open(self.fileName, 'rb')
			self.CHUNK = 1024
			self.FORMAT = p.get_format_from_width(wf.getsampwidth())
			self.CHANNELS = wf.getnchannels()
			self.RATE = wf.getframerate()
			self.isOpened = True

	# disable_readMode : disable readMode and close the file.
	def disable_readMode(self) :
		if self.isFromFile == True :
			self.wf.close()
			self.isOpened = False

	# enable_continuousReading : enables continuous chunk acquisition from input device.
	# /!\ sets also environment values so watch out to disable readMode first. 
	# 		To switch from file reading mode to record mode : switchReadRecordMode
	def enable_continuousReading(self) :
		self.isContinuousReading = True
		self.stream = self.p.open(format = self.FORMAT,
                channels = self.CHANNELS,
                rate = self.RATE,
                input=True,
                frames_per_buffer=self.CHUNK)

	# disable_continuousReading : disables continuous reading and releases the input device.
	def disable_continuousReading(self) :
		self.isContinuousReading = False
		self.stream.stop_stream()
		self.stream.close()
		
