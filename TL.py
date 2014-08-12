# Main file of the project !

# Last modification : Loic

import sys
import signal
sys.path.insert(0, 'src/')
from configs import Config_manager 
from audio import audio_core
from NC import NC_manager
from network_udp import UDP_network_manager

#global state
state = "New_matrice"

#global new_matrice_created
new_matrice_created = False

#global decoded
decoded = False

# Stating point of the progtramm
# Get the parameters
configs = Config_manager()
# store them in the configs manager
configs.parse()

# Hello message
print "--"
print "Starting.."
print "--\n"

# start the modules according to configs
if configs.args.relay:
	configs.verbose_message("Start as a relay")
	
elif configs.args.source:
	configs.verbose_message("Start as a source")

elif configs.args.sink:
	configs.verbose_message("Start as a sink")

else:
	print 'You should specify a mode. See help.\n'
	exit()

# Send function
def sending_source():
	global new_matrice_created
	global state
	# If has to send new matrice info
	if state == "New_matrice":
		configs.verbose_message('Sending new matrice info')
		if not new_matrice_created:
			configs.verbose_message('Creating coefs')
			nc.Encode(audio.Read())
			new_matrice_created = True
		return 'New_matrice'
	# If has to send coded packets
	else:
		configs.verbose_message('Sending coded packet')
		return nc.Get_packet()

def sending():
	if configs.args.relay:
		configs.verbose_message('Cannot send in relay mode !')
		return False
	elif configs.args.sink:
		configs.verbose_message('Cannot send in sink mode !')
		return False
	else:
		return sending_source()

# Processing data :
def process_sink(data):
	global decoded
	configs.verbose_message('Receiving data and process it !')
	#If new matrice arriving
	if data == 'New_matrice':
		nc.New_decoder()
		configs.verbose_message('New matrice incomming !')
		nm.Send_to_all('OK')
		decoded = False
	#Else
	else:
		if decoded:
			configs.verbose_message('Everything is here but, resend ok2')
			nm.Send_to_all('OK2')
		else:
			configs.verbose_message('Trying to decode')
			if nc.Decode(data):
				configs.verbose_message('Decode ok !')
				nm.Send_to_all('OK2')
				decoded = True
		
		
def process_source(data):
	global new_matrice_created
	global state
	configs.verbose_message('Getting data from someone !')
	# If ('OK') then send coded packets
	if data == 'OK' and state == "New_matrice":
		state = "Not_new_matrice"
		configs.verbose_message('OK received, state = Not_new_matrice')

	# Else if ('OK2') then start new matrice
	elif data == 'OK2':
		state = "New_matrice"
		configs.verbose_message('All received, proceed new matrice')
		new_matrice_created = False

def process_relay(data):
	configs.verbose_message('Transferring data !')
	nm.Send_to_all(data)

def process(data):
	if configs.args.relay:
		process_relay(data)
	elif configs.args.sink:
		process_sink(data)
	else:
		process_source(data)

# Start audio if not relay
audio = audio_core()

# Start the NC manager
nc = NC_manager(10, 512)

# Start the network manager
nm = UDP_network_manager('', '127.0.0.1', 12000, sending, process)
nm.Start_listenning()

# Listen system interrupt
def closing(arg1, arg2):
	nm.Close()
	audio.stop_audioCore()
	# Bye message
	print "--"
	print "Bye bye"
	print "--\n"

signal.signal(signal.SIGINT, closing)
# Infinite loop
while 1:
	nm.Network_magic()

