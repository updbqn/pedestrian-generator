import ProSivicDDS
import os
from time import sleep


def callback(x):
    print("callback called!")
    return


def callbackEnv(x):
    print("callbackEnv called!")
    print(x)
    return


# initialise dds communication
carOrder = ProSivicDDS.carOrderHandler("audi/car", callback)
carEnv = ProSivicDDS.carEnvironmentHandler("audi/car", callbackEnv)

while 1:
    sleep(1)
    print("loop")


# pause program
os.system("pause")
