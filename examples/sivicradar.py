import ProSivicDDS as psv
import os
from time import sleep

# initialise dds car order communication
radarreceiver = psv.radarHandler("radarLevel1/radar")
sleep(0.100)
targetS = radarreceiver.receive()
targetlist = targetS.data
target0 = targetlist[0]
print(target0.distance)
# pause program
os.system("pause")
