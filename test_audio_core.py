# Test section of audio_core class
# Last Modificication from D3Rnatch

import sys
import time
sys.path.insert(0, 'src/')
from audio import *

# creating and starting the audio core system.
# has record mode.
audio = audio_core()

frames = []

# we get 500 chunks from audio input device
# but first enable continuous reading is necessary !
# audio.enable_continuousReading()

for i in range(0,100) :
	data = audio.Read()
	frames.append(data)

audio.createWaveFile("test.wav", frames) 

# we play those 500 chunks directly
#audio.disable_continuousReading()
audio.enable_continuousPlay()

for i in range(0,100) :
	audio.Play(frames[i])
	#time.sleep(0.01)

# we close the audio core
audio.stop_audioCore()

# uncomment this section to test reading file mode

# restarting the audio core

# we read the file, until data == -1

# we output the file 

# we close the stuff 



