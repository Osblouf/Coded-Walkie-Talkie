# This module will manage configurations

# Last modification : Loic 
from datetime import datetime
import argparse

class Config_manager:

	# Constructor
	def __init__(self):
		self.parser = argparse.ArgumentParser(
			description='This program is running on a raspberry pi to demonstrate the usage of network coding in a simple application : walkie talkie.',
			epilog='Examples comming soon')
		self.parser.add_argument('-d', '--debug', action='store_true',
			help='Set this argument to have a debug info in the log file')
		self.parser.add_argument('-v', '--verbose', action='store_true',
			help='Set this argument to have ALL messages print on the command line.')
		self.parser.add_argument('-r', '--relay', action='store_true',
			help='Set this argument to have the device running as a relay.')
		self.parser.add_argument('-R', '--recode', action='store_true',
			help='Set this argument to recode if the device is a relay.')
		self.parser.add_argument('-m', '--coding_mode', nargs=1, default=0, type=int, choices=range(0, 3), metavar='MODE',
			help='Configure the coding mode : 0 no coding, 1 coding full, 2 coding on the fly, 3 windowed coding.' )
		self.parser.add_argument('-s', '--source', action='store_true', 
			help='Set this argument to act like a source.')
		self.parser.add_argument('-S', '--sink', action='store_true', 
			help='Set this argument to act like a sink.')
		self.parser.add_argument('-f', '--file', nargs=1, type=file, metavar = 'FILE_NAME', 
			help='Specify the input file if act like a source. If no file specified, the device will try to read the mic port instead.')

	# Get all infos from the command line
	def parse(self):
		self.args = self.parser.parse_args()
		if self.args.verbose:
			print "\nGiven arguments: "
			print self.args 
			print "--\n"
		
	# Manage the verbose messages
	def verbose_message(self, message):
		if self.args.verbose:
			print '[' + datetime.utcnow().strftime('%H:%M:%S.%f') + '] Verbose message :'
			print "\t" + message

	# Manage the debug messages
	def debug_message(self, message):
		if self.args.debug:
			print '[' + datetime.utcnow().strftime('%H:%M:%S.%f') + '] Debug message :'
			print '\t' + message

	# Getting the file name
	def get_file_name(self):
		return self.args.file
