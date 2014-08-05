# Main file of the project !

# Last modification : Loic
import sys
sys.path.insert(0, 'src/')
from configs import Config_manager 

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
	
if configs.args.source:
	configs.verbose_message("Start as a source")

if configs.args.sink:
	configs.verbose_message("Start as a sink")

# Bye message
print "--"
print "Bye bye"
print "--\n"
