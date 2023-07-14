import paho.mqtt.client as mqtt
import time
from gpiozero import LED
import requests
import json

led1 = LED(26)
print ("listening for messages on topic: cesmii/lab1 ...")

def on_message(client, userdata, message):
	msg = str(message.payload.decode("utf-8"))
	print("received message: " , msg)
	if msg == "on":
		led1.on()
	elif msg == "off":
		led1.off()
	else:
		print("no GPIO message")

mqttBroker = "192.168.1.8"

client = mqtt.Client("smartmfgcli2")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("cesmii/lab1")
client.on_message=on_message

client.loop_forever()
