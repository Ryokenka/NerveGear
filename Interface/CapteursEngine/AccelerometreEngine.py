import serial
import paho.mqtt.client as mqtt

def AccelerometreTracking(func_action_avant=None, func_action_arrière=None, func_action_gauche=None, func_action_droite=None, func_action_milieu=None):
	ser = serial.Serial('COM7', 115200, timeout=1)
	Client = mqtt.Client("AccelerometerEngine")
	while True:
		data = ser.readline().decode('utf-8').strip()
		print(data)
		if data == "DEVANT":
			if func_action_avant is not None:
				func_action_avant()
		elif data == "DERRIERE":
			if func_action_arrière is not None:
				func_action_arrière()
		elif data == "Gauche":
			if func_action_gauche is not None:
				func_action_gauche()
		elif data == "droite":
			if func_action_droite is not None:
				func_action_droite()
		else :
			func_action_milieu()
	ser.close()
