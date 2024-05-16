import numpy as np
import time
from bitalino import *
from matplotlib import pyplot as plt


def MuscleTracking(func_action_1=None, func_action_longue=None):
	# Windows
	macAddress = "98:D3:81:FD:63:49"
	clicklong= False
	device = BITalino(macAddress)
	time.sleep(1)

	srate = 1000
	nframes = 1000
	threshold = 40

	# ===============  ========= ========= ========= ========= ========
	# Sequence Number    BTN       -----     LED       BUZ       EMG
	# ===============  ========= ========= ========= ========= ========
	#  0                1         2         3         4         5

	device.start(srate, [3])
	print("START")
	try:
		while True:
			data = device.read(nframes)
			if np.mean(data[:, 1]) < 1: break
			EMG = data[:, -1]
			envelope = np.mean(abs(np.diff(EMG)))

			if envelope > threshold:
				if clicklong & (func_action_longue is not None):
					func_action_longue()
					print("Envelope 2 detected")
				else :
					clicklong = True
					device.trigger([0, 1])
					if func_action_1 is not None:
						func_action_1()
						print("Envelope detected")
			else:
				clicklong = False
				device.trigger([0, 0])
				print("Envelope NON")

	finally:
		print("STOP")
		device.stop()
		device.close()

def handlePression():
	print("Clicked")

def handleDoubledPression():
	print("Double Clicked")
