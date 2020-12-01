import ProSivicDDS as psv
import os
import numpy as np
from skimage import data
from skimage.viewer import ImageViewer

# initialise dds communication to Pro-SiVIC object named "camera/cam"
cam = psv.cameraHandler("camera/cam")

# get the last frame emitted
image = cam.receive()

# transform image as numpy array, directly accessing image data
imagenp = np.array(image, copy=False)

# display image
viewer = ImageViewer(imagenp)
viewer.show()

os.system("pause")
