#!/bin/bash
echo "Waiting for network..."
sleep 10
/usr/bin/python3 /home/pi/mqtt-listen-graphql.py & >/home/pi/logs/startuplog 2>&1
echo "MQTT ready!"

