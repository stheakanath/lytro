# Kuriakose Sony Theakanath
# Depth Refocusing

import numpy as np
import glob
from PIL import Image
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2

LOTS = 290

def depthRefocusing(path, SCALE):
	w, h = Image.open("size.png").size
	arr = np.zeros((h, w, 3),np.float)
	for fname in glob.glob(path):
		print fname
		x, y = int(fname.split("_")[1]), int(fname.split("_")[2])
		shiftx, shifty = (8 - x) * SCALE, (8 - y) * SCALE
		print(shiftx, shifty)
		M = np.float32([[1, 0, shifty], [0, 1, shiftx]])
		item = np.array(Image.open(fname), dtype=np.float)
		dst = cv2.warpAffine(item, M, (w, h))
		arr = arr + dst / LOTS
	arr = np.array(np.round(arr), dtype=np.uint8)
	Image.fromarray(arr, mode="RGB").save("-1.png")

def aperture(path, num):
	w, h = Image.open("size.png").size
	arr = np.zeros((h, w, 3),np.float)
	for fname in glob.glob(path):
		item = np.array(Image.open(fname), dtype=np.float)
		arr = arr + item / num
	arr = np.array(np.round(arr), dtype=np.uint8)
	Image.fromarray(arr, mode="RGB").save("aperture_" + str(num) + ".png")

# depthRefocusing("rectified/*.png", -1)
aperture("apeture209/*.png", 209)