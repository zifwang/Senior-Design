# Senior-Design-Code
# This code is for testing light sensor

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
light_sensor_output = ""

# define the pin that goes to the circuit
# Modify based on the PCB
pin_to_circuit1 = 14 #light out
pin_to_circuit2 = 15 #clk
pin_to_circuit3 = 18 #cs

#pin_to_circuit9 = 25 #Light sensor output
#EOC = 4 #End of Conversion signal - goes low during conversion
#clock = 4
#ALE = 12

#pin_to_circuitA = 17 #MUX control bits
#pin_to_circuitB = 27
#pin_to_circuitC = 22


#Configure to inputs
GPIO.setup(pin_to_circuit1, GPIO.IN)
GPIO.setup(pin_to_circuit2, GPIO.OUT)
GPIO.setup(pin_to_circuit3, GPIO.OUT)

#GPIO.setup(pin_to_circuit9, GPIO.IN)
#GPIO.setup(EOC, GPIO.IN)

#Control Signals
#GPIO.setup(clock,GPIO.ALT0)
#GPIO.setup(ALE,GPIO.OUT)
#GPIO.setclock(clock,500000) #500KHz
#GPIO.output(clock,1)

#MUX controls - set to low
##GPIO.setup(pin_to_circuitA, GPIO.OUT)
##GPIO.setup(pin_to_circuitB, GPIO.OUT)
##GPIO.setup(pin_to_circuitC, GPIO.OUT)

#GPIO.output(pin_to_circuitA, 0)
#GPIO.output(pin_to_circuitB, 0)
#GPIO.output(pin_to_circuitC, 0)

while True:
 #   light_sensor_output = ""

    GPIO.output(ALE,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(ALE,GPIO.LOW)
    time.sleep(1)
    
    a_LSB = float(GPIO.input(pin_to_circuit1))
    #light_sensor_output = light_sensor_output + str(a)
    print("LSB: ", a_LSB)
        
    a_1 = float(GPIO.input(pin_to_circuit2))
    #light_sensor_output = light_sensor_output + str(a)
    print("Bit: ", a_1)

    a_2 = float(GPIO.input(pin_to_circuit3))
    #light_sensor_output = light_sensor_output + str(a)
    print("Bit: ", a_2)
        
    a_3 = float(GPIO.input(pin_to_circuit4))
    #light_sensor_output = light_sensor_output + str(a)
    print("Bit: ", a_3)

    a_4 = float(GPIO.input(pin_to_circuit5))
    #light_sensor_output = light_sensor_output + str(a)
    print("Bit: ", a_4)

    a_5 = float(GPIO.input(pin_to_circuit6))
    #light_sensor_output = light_sensor_output + str(a)
    print("Bit: ", a_5)
        
    a_6 = float(GPIO.input(pin_to_circuit7))
    #light_sensor_output = light_sensor_output + str(a)
    print("Bit: ", a_6)

    a_MSB = float(GPIO.input(pin_to_circuit8))
    #light_sensor_output = light_sensor_output + str(a)
    print("MSB: ", a_MSB)

    a_7 = float(GPIO.input(pin_to_circuit9))
    #light_sensor_output = light_sensor_output + str(a)
    print("Actual analog output: ", a_7)

    #a_8 = float(GPIO.input(EOC))
    #print("End of conversion bit: ", EOC)
        
    # print(light_sensor_output)


GPIO.setwarnings(disable)
