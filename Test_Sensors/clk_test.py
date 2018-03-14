#test clock
#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

def convert_to_tens(digit_array):
   result = 0
   length = len(digit_array)
   t0 = 0
   while (t0<length):
      t1 = digit_array[t0]

      t2 = length - 1
      t2 = t2 - t0
      while(t2>0):
         t1 = t1 * 2
         t2 = t2 - 1
      result = result + t1
      t0 = t0 + 1
   return result

GPIO.setmode(GPIO.BCM)
pin_to_circuit1 = 4 #clock signal
pin_to_circuit2 = 17 #CS
pin_to_circuit3 = 27 #Data

data = []

GPIO.setup(pin_to_circuit1, GPIO.OUT)
GPIO.setup(pin_to_circuit2, GPIO.OUT)
GPIO.setup(pin_to_circuit3, GPIO.IN)

GPIO.output(pin_to_circuit2, GPIO.HIGH)
time.sleep(0.5)

for j in range(0,1):
   GPIO.output(pin_to_circuit2, GPIO.LOW)
   for i in range(0,16): 
      time.sleep(0.1)
      GPIO.output(pin_to_circuit1, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(pin_to_circuit1, GPIO.HIGH)


      data.insert(i,GPIO.input(pin_to_circuit3))
      print(GPIO.input(pin_to_circuit3))

   GPIO.output(pin_to_circuit2, GPIO.HIGH)


GPIO.setwarnings(False)

del data[12:16]
del data[0:4]
print(data)
answer = convert_to_tens(data)
print(answer)
