# Senior-Design-Code
# This code is to generate high frequency output signal

import RPi.GPIO as GPIO
import time

# Enable pigpio
# Require "sudo pigpiod" in terminals
import pigpio

GPIO.setmode(GPIO.BCM)

# output pin in pi
clock_signal = 4

square = []

square.append(pigpio.pulse(1<<clock_signal, 0, 4))
square.append(pigpio.pulse(0, 1<<clock_signal, 4))

pi = pigpio.pi()

pi.set_mode(clock_signal, pigpio.OUTPUT)

pi.wave_add_generic(square)

wid = pi.wave_create()

if wid >= 0:
    pi.wave_send_repeat(wid)
    time.sleep(60)
    pi.wave_tx_stop()
    pi.wave_delete(wid)

pi.stop()

