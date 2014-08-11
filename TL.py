# Main file of the project !

# Last modification : Loic

import sys
import signal
sys.path.insert(0, 'src/')
from configs import Config_manager 
from audio import audio_core
from NC import NC_manager
from network_udp import UDP_network_manager

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
state = "New_matrice"
new_matrice_created = False
def sending_source():
	# If has to send new matrice info
	if state == "New_matrice":
		configs.verbose_message('Sending new matrice info')
		nm.Send_to_all('New_matrice')
		if not new_matrice_created:
			configs.verbose_message('Creating coefs')
			nc.Encode(audio.Read())
			new_matrice_created = True

	# If has to send coded packets
	else:
		configs.verbose_message('Sending coded packet')
		nm.Send_to_all(nc.Get_packet())

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
decoded = False
def process_sink(data):
	configs.verbose_message('Receiving data and process it !')
	#If new matrice arriving
	if data == 'New_matrice':
		nm.Send_to_all('OK')
		decoded = False
	#Else
	else:
		if decoded:
			nm.Send_to_all('OK2')
		else:
			if nc.decode(data):
				nm.Send_to_all('OK2')
				decoded = True
		
		
def process_source(data):
	configs.verbose_message('Getting data from someone !')
	# If ('OK') then send coded packets
	if data == 'OK':
		state = "Not_new_matrice"

	# Else if ('OK2') then start new matrice
	elif data == 'OK2':
		state = "New_matrice"
		new_matrice_created = False

def process_relay(data):
	configs.verbose_message('Transferring data !')
	nm.Send_to_all(data)

def process(data):
	if configs.args.relay:
		process_relay()
	elif configs.args.sink:
		process_sink()
	else:
		process_source()

# Start audio if not relay
audio = audio_core(configs.get_file_name)

# Start the NC manager
nc = NC_manager(10, 1024)

# Start the network manager
nm = UDP_network_manager('', '127.0.0.1', 12000, process, sending)
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

