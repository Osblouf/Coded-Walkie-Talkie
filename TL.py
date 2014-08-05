# Main file of the project !

# Last modification : Loic
import sys
sys.path.insert(0, 'src/')
from configs import Config_manager 

# Stating point of the progtramm
# Get the parameters
configs = Config_manager()
#store them in the configs manager
configs.parse()
