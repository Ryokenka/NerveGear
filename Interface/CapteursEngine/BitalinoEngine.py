import numpy as np
import time
from bitalino import *

def MuscleTracking(MC):
	# Windows
	macAddress = "98:D3:81:FD:63:49"

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
				device.trigger([0, 1])
				MC.mouvement_clic_muscle()
				print("Envelope detected")
			else:
				device.trigger([0, 0])
				print("Envelope NON")

	finally:
		print("STOP")
		device.stop()
		device.close()



