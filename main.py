# Senior-Design-Code
# Main function

import PRi.GPIO as GPIO            # Enable GPIO
import time                        # Enable time 
import numpy as np                 # Enable numpy array
import matplotlib.pyplot as plt    # Enable plot function
import getch                       # Enable get_character
import sys                         # Enable exit function
from matplotlib.ticker import NullFormatter 


GPIO.setmode(GPIO.BCM)             # Set GPIO output pins format

############################################################
# Define input pins
# define the input pins that goes to the circuit
# Modify based on the PCB
PIR_pin =  # PIR sensor into raspberry pi

temp_pin =   #Tempature & humndity sensor data into raspberry pi

light_pin =  # Light sensor data into raspberry pi

light_clk =  # CLK input into light sensor

light_cs =  # CS input into light sensor

light_control_pin = # light control pin 

#############################################################

#############################################################
# Create a data structure to store data from sensors
# This is a map has built-in function:
#          - add_data function is used to add new data into data structure
#          - get function is used to get each data list in data structure
#          - print_last_data function is used to print the current data
#          - print_data function is used to print all the data in each list 
#          - draw_data function is used to draw data graph of each data list
class Mapping:

    def __init__(self, name):
        self.name = name
         # initialize 4 lists to hold data
        self.tem_list = []   # temperature list
        self.hum_list = []   # humidity list
        self.lgt_list = []   # illumance list
        self.PIR_list = []   # PIR list

    def add_data(self, key, value):
        # This function is used to add data into lists
        # Call this function to add: self.add(key,value) in main function 
        # Four cases: temperature, humidity, light, and PIR
        # In order to make this class to work, the key must be 
        # enter as tem, hum, lgt, pir
        if(key == 'tem'):
            self.tem_list.append(value)
        elif(key == 'hum'):
            self.hum_list.append(value)
        elif(key == 'lgt'):
            self.lgt_list.append(value)
        elif(key == 'pir'):
            self.PIR_list.append(value)
        else:
            print("List not found")

    def get(self,key):
        # This function is to get values in list
        # Require enter self.get(key) in main function
        # In order to make this class to work, the key must be 
        # enter as tem, hum, lgt, pir
        result = []
        if(key == 'tem'):
            result =  self.tem_list
        elif(key == 'hum'):
            result =  self.hum_list
        elif(key == 'lgt'):
            result =  self.lgt_list
        elif(key == 'pir'):
            result =  self.PIR_list
        else: 
            print("List not found")
            result = [None]
        return result     # return a none list

    def print_last_data(self,key):
        # This function is to print values in each list
        # Require enter self.print_last_data(key) in main function
        # In order to make this class to work, the key must be 
        # enter as tem, hum, lgt, pir, or all
        if(key == 'tem'):
            print("Current Temperature: ", self.tem_list[-1])
        elif(key == 'hum'):
            print("Current Humidity: ", self.hum_list[-1])
        elif(key == 'lgt'):
            print("Current Illuminance Level: ", self.lgt_list[-1])
        elif(key == 'pir'):
            pir = self.PIR_list[-1]
            if(pir == 1):
                print("There is people in the room right now.")
            else:
                print("Room is empty right now")
        elif(key == 'all'):
            print("Current Temperature: ", self.tem_list[-1])
            print("Current Humidity: ", self.hum_list[-1])
            print("Current Illuminance Level: ", self.lgt_list[-1])
            pir = self.PIR_list[-1]
            if(pir == 1):
                print("There is people in the room right now.")
            else:
                print("Room is empty right now")

    def print_data(self,key):
        # This function is to print values in each list
        # Require enter self.print_data(key) in main function
        # In order to make this class to work, the key must be 
        # enter as tem, hum, lgt, pir, or all
        if(key == 'tem'):
            print("Temperature data display:")
            print(self.tem_list)
        elif(key == 'hum'):
            print("Humidity data display:")
            print(self.hum_list)            
        elif(key == 'lgt'):
            print("Illuminance data display:")
            print(self.lgt_list)
        elif(key == 'pir'):
            print("PIR sensor data display:")
            print(self.PIR_list)
        elif(key == 'all'):
            print("Temperature data display:")
            print(self.tem_list)
            print("Humidity data display:")
            print(self.hum_list)
            print("Illuminance data display:")
            print(self.lgt_list)
            print("PIR sensor data display:")
            print(self.PIR_list)
        else: 
            print("List not found")

    def table_data(self,key):
        print("Data display as a table")

    def draw_data(self,key):
        # This function is to draw data from list
        # Call this function in main to display data graph
        # key: tem, hum, lgt, pir, all
        # all key is to draw all data in a picture by using subplot
        
        data = []         # generate a data list

        if (key == 'tem'):
            data = self.tem_list
            #Plot function
            plt.plot(data)
            # Setting title 
            plt.title(r'Temperature', fontsize=20)
            # Set x and y labels
            plt.xlabel('time')
            plt.ylabel('temperature')
            # show image
            plt.show()
        elif (key == 'hum'):
            data = self.hum_list
            #Plot function
            plt.plot(data)
            # Setting title 
            plt.title(r'Humidity', fontsize=20)
            # Set x and y labels
            plt.xlabel('time')
            plt.ylabel('humidity')
            # show image
            plt.show()
        elif (key == 'lgt'):
            data = self.lgt_list
            #Plot function
            plt.plot(data)
            # Setting title 
            plt.title(r'Illuminance', fontsize=20)
            # Set x and y labels
            plt.xlabel('time')
            plt.ylabel('illuminance')
            # show image
            plt.show()
        elif (key == 'pir'):
            data = self.PIR_list
            #Plot function
            plt.plot(data)
            # Setting title 
            plt.title(r'PIR', fontsize=20)
            # Set x and y labels
            plt.xlabel('time')
            plt.ylabel('PIR')
            # show image
            plt.show()
        elif (key == 'all'):
            # print("Key all entered")
            # Get all data
            data_tem = self.tem_list
            data_hum = self.hum_list
            data_lgt = self.lgt_list
            data_pir = self.PIR_list
            # plot with various axes scales
            plt.figure(1)

            # Temperature
            plt.subplot(221)
            plt.plot(data_tem)
            plt.ylabel('temperature')
            plt.xlabel('time')
            plt.title('Temperature')

            # Humidity
            plt.subplot(222)
            plt.plot(data_hum)
            plt.ylabel('humidity')
            plt.xlabel('time')
            plt.title('Humidity')     

            # Illuminance
            plt.subplot(223)
            plt.plot(data_lgt)
            plt.ylabel('illuminance')
            plt.xlabel('time')
            plt.title('Illuminance')    

            # PIR
            plt.subplot(224)
            plt.plot(data_pir)
            plt.ylabel('PIR')
            plt.xlabel('time')
            plt.title('PIR')    

            # Format the minor tick labels of the y-axis into empty strings with
            # `NullFormatter`, to avoid cumbering the axis with too many labels.
            #plt.gca().yaxis.set_minor_formatter(NullFormatter())
            # Adjust the subplot layout, because the logit one may take more space
            # than usual, due to y-tick labels like "1 - 10^{-3}"
            plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

            # image show 
            plt.show()
                  
        else:
            print("Key entered is not found")
#############################################################

#############################################################
# keyboard interrupt 
# get user input while running program
# enter 'h' open help table
# enter 'd' to select which sensors' graph to draw
# enter 'l' to control light
# enter 's' to stop monitor 
# enter 'p' to print current data 
def get_user_input():
    c = getch.getch()

    if(c == 'h'):
        # help table printing
        help_printing()
    elif(c == 's'):
        # Stop the program
        sys.exit()
    elif(c == 'l'):
        # Light control
        char = input("Do you want to turn on or turn off the light? --enter on to turn on the light or off to turn off: ")
        if(char == 'on'):
            # In PI, define the output pin to turn on the light
            print("light is on")
        else: 
            print("light is off")
    elif(c == 'd'):
        # display graph
        char = input("Graph Display, enter 'tem' for temperature graph, 'hum' for humidity graph, 'lgt' for illuminance level graph, 'pir' for Motion graph, 'all' for display all four data: ")
        d.draw_data(char)
    elif(c == 'p'):
        char = input("Current Data Display, enter 'tem' for temperature, 'hum' for humidity, 'lgt' for illuminance level, 'pir' for human motion, 'all' to display all data: ")
        d.print_last_data(char)
    else:
        # Command not found
        print("Wrong command")
        # When user enter a wrong command, display the help table
        help_printing()
#############################################################

#############################################################
# help table    
def help_printing():
    print("Options                          Description")
    print("h                          For printing avaliable commands")
    print("l                                Light Control")
    print("d                                Graph Display")
    print("p                              Print Current Data")
    print("s                                 Stop Program")
#############################################################


# PIR_pin =  # PIR sensor into raspberry pi

# temp_pin =   #Tempature & humndity sensor data into raspberry pi

# light_pin =  # Light sensor data into raspberry pi

# light_clk =  # CLK input into light sensor

# light_cs =  # CS input into light sensor
#############################################################
# Collect data from light sensor
# convert_to_tens function is used to convert binary number into decimal
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
   
# use def here to build function
def data_from_light_sensor():
    # create a list of binary data
    data = []
    # GPIO pin set up
    GPIO.setup(light_clk, GPIO.OUT)
    GPIO.setup(light_cs, GPIO.OUT)
    GPIO.setup(light_pin, GPIO.IN)
    # Set ligth_cs to be high to start up light sensor
    GPIO.output(light_cs, GPIO.HIGH)
    # Give a time for light sensor to be stable
    time.sleep(0.5)

    # Collecting data
    for j in range(0,1):
        # Set light_cs to be low to start collecting data
        GPIO.output(light_cs, GPIO.LOW)
        for i in range(0,16): 
            time.sleep(0.1)
            GPIO.output(light_clk, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(light_clk, GPIO.HIGH)
            # put data into list
            data.insert(i,GPIO.input(light_pin))
        # Set light_cs back to high again
        GPIO.output(light_cs, GPIO.HIGH)

    # the first 5 bits and the last 5 bits are useless
    del data[12:16]
    del data[0:4]

    # Convert data to decimal 
    result = convert_to_tens(data)
    return result
#############################################################

#############################################################
# Collect data from PIR sensor
# use def here to build function
def data_from_PIR_sensor():
    result = float(GPIO.input(PIR_pin))
    return result
#############################################################

#############################################################
# Collect data from Temperature senor
# use def here to build function





#############################################################
if __name__ == "__main__":
    # print help function



    # declare the data struct



    # while_loop goes to here 
        # Push light sensor data to data struct

        # Push PIR sensor data to data struct

        # Push Temperature sensor data to data struct

        # get user input







