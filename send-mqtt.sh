#!/bin/bash
USE_DATE=`date`
USE_MSG="Test message at $USE_DATE"
if [[ ! -z "$1" ]]; then
	USE_MSG=$1
fi
echo Sending message: $USE_MSG
mosquitto_pub -h 192.168.1.8 -t "cesmii/lab1" -m "$USE_MSG"
