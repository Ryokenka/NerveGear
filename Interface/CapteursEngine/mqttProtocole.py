import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc, properties):
	print("Connected with result code " + str(rc))
	client.subscribe("MIN1")


def on_message(client, userdata, msg):
	print(msg.topic + " " + str(msg.payload))


client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

host = "54.38.241.241"

client.connect(host, 1883, 60)

client.loop_forever()
