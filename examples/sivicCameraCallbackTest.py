import ProSivicDDS as psv
import os
import time
import numpy as np
import matplotlib.image as mpimg

# set  DDS configuration file location
psv.initcomms("config.json")


def callback(x):
    npx = np.array(x, copy=False)
    print(x.timestamp)
    name = "cam" + str(x.timestamp) + ".png"
    # uncomment to save image
    mpimg.imsave(name, npx)


# initialise dds communication to Pro-SiVIC object named "camera/cam"
cam = psv.cameraHandler("camera/cam", callback)

while 1:
    time.sleep(0.1)

os.system("pause")
