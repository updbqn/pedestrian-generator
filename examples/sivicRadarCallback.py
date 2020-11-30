import ProSivicDDS as psv
import os
from time import sleep

def radarFrameCallback(x):
    print(x[0])
    return

#initialise dds car order communication
radarreceiver =psv.radarHandler('radarLevel1/radar',radarFrameCallback)

while 1:
    sleep(0.100)

#pause program
os.system("pause")


