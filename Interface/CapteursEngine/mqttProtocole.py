import paho.mqtt.client as mqtt


class MqttProtocole:

	def __init__(self):
		self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message
		self.host = "54.38.241.241"
		self.msg = ""
	def on_connect(self,client, userdata, flags, rc, properties):
		print("Connected with result code " + str(rc))
		client.subscribe("MIN1")

	def on_message(self,client, userdata, msg):
		print("Received message: ", msg.payload.decode())
		self.msg = msg.payload.decode()
		return msg.payload.decode()

	def connect(self):
		self.client.connect(self.host, 1883, 60)
		self.client.loop_start()

	def disconnect(self):
		self.client.disconnect()
		print("Disconnected from broker")

	def publish(self, topic, message):
		self.client.publish(topic, message)
		print("Published message: ", message, " on topic: ", topic)

	def subscribe(self, topic):
		self.client.subscribe(topic)
		print("Subscribed to topic: ", topic)

	def unsubscribe(self, topic):
		self.client.unsubscribe(topic)
		print("Unsubscribed to topic: ", topic)


if __name__ == "__main__":
	mqtt = MqttProtocole()
	mqtt.connect()
	mqtt.publish("MIN1", "Hello World")

