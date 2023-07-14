#!/bin/bash
echo "Listening for topic: cesmii/lab1"
mosquitto_sub -h 192.168.1.8 -t "cesmii/lab1"
