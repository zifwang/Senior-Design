# Senior-Design-Code
# This code is for testing the temperature sensor
# This code is only for temperature not humandity

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_to_circuit = 4

#Configure to input
GPIO.setup(pin_to_circuit, GPIO.IN)

while True:
    a = float(GPIO.input(pin_to_circuit))
    print(a)

GPIO.setwarnings(disable)

