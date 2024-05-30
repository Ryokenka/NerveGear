import serial

import paho.mqtt.client as mqtt


def AccelerometreTracking(func_action_avant=None, func_action_arrière=None, func_action_gauche=None,
						  func_action_droite=None, func_action_milieu=None):
	def on_connect(client, userdata, flags, rc, properties):
		print("Connected with result code " + str(rc))
		client.subscribe("MIN1")

	def on_message(client, userdata, msg):
		print(msg.topic + " " + str(msg.payload))
		message = msg.payload.decode()
		if message is not None:
			if message == 'AVANT':
				if func_action_avant is not None:
					func_action_avant()
			elif message == 'ARRIERE':
				if func_action_arrière is not None:
					func_action_arrière()
			elif message == 'GAUCHE':
				if func_action_gauche is not None:
					func_action_gauche()
			elif message == 'DROITE':
				if func_action_droite is not None:
					func_action_droite()
			else:
				func_action_milieu()

	print("AccelerometreTracking")
	# ser = serial.Serial('COM7', 115200, timeout=1)

	client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
	client.on_connect = on_connect
	client.on_message = on_message

	host = "54.38.241.241"
	client.connect(host, 1883, 60)
	client.loop_start()


	# while True:
	# 	data = ser.readline().decode('utf-8').strip()
	# 	print(data)
	# 	if data == "DEVANT":
	# 		if func_action_avant is not None:
	# 			func_action_avant()
	# 	elif data == "DERRIERE":
	# 		if func_action_arrière is not None:
	# 			func_action_arrière()
	# 	elif data == "Gauche":
	# 		if func_action_gauche is not None:
	# 			func_action_gauche()
	# 	elif data == "droite":
	# 		if func_action_droite is not None:
	# 			func_action_droite()
	# 	else:
	# 		func_action_milieu()
	# ser.close()
