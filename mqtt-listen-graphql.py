import paho.mqtt.client as mqtt
import time
from datetime import datetime
from gpiozero import LED
from smip import graphql
import requests
import json

led1 = LED(26)
mqtt_broker = "192.168.1.8"
mqtt_topic = "cesmii/lab1"
mqtt_client = "inAMeeting"
graphql = graphql("Ben", "Wise", "cesmiihq", "ncsu_graphql", "https://ncsu.cesmii.thinkiq.net/graphql")

print (f"Listening for MQTT messages on topic: {mqtt_topic} ...")

def make_datetime_utc():
	utc_time = str(datetime.utcnow())
	time_parts = utc_time.split(" ")
	utc_time = "T".join(time_parts)
	time_parts = utc_time.split(".")
	utc_time = time_parts[0] + "Z"
	return utc_time

def update_smip(light_on):
	print("Requesting Data from CESMII Smart Manufacturing Platform...")
	print()
	utcTime = make_datetime_utc()
	print("Using datetime as: " + str(utcTime))
	smp_query = f"""
                mutation updateTimeSeries {{
                replaceTimeSeriesRange(
                    input: {{attributeOrTagId: "10926", entries: [ {{timestamp: "{make_datetime_utc()}", value: "{light_on}", status: "1"}} ] }}
                    ) {{
                    clientMutationId,
                    json
                }}
                }}
            """
	smp_response = ""

	try:
		smp_response = graphql.post(smp_query)
	except requests.exceptions.HTTPError as e:
		print("An error occured accessing the SM Platform!")
		print(e)

	print("Response from SM Platform was...")
	print(json.dumps(smp_response, indent=2))
	print()

def on_message(client, userdata, message):
	msg = str(message.payload.decode("utf-8"))
	print("received MQTT message: ", msg)
	if msg == "on":
		led1.on()
		update_smip("true")
	elif msg == "off":
		led1.off()
		update_smip("false")
	else:
		print("no valid GPIO message")

client = mqtt.Client(mqtt_client)
client.connect(mqtt_broker)
client.loop_start()
client.subscribe(mqtt_topic)
client.on_message=on_message
client.loop_forever()
