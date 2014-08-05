# Main file of the project !

# Last modification : Loic
import sys
sys.path.insert(0, 'src/')
from configs import Config_manager 

# Stating point of the progtramm

configs = Config_manager()

configs.parse()
