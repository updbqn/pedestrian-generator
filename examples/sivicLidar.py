import ProSivicDDS as psv
import os
from time import sleep

#initialise dds car order communication
lidarConfigreceiver =psv.lidarconfigHandler("laserScanner/lsr")
sleep(0.100)
config = lidarConfigreceiver.receive()

lidarDatareceiver =psv.lidardataHandler("laserScanner/lsr")
sleep(0.100)
data=lidarDatareceiver.receive()
while(data.timestamp==0):
    data=lidarDatareceiver.receive()

print(data.distance)
#pause program
os.system("pause")


