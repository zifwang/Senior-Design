# Test map & plot function in python
# import numpy as np                      # Enable numpy array
# import matplotlib.pyplot as plt         # Enable plot function

# # Set two variables
# tem = [23,24,25,24]            # tempertature
# s = [0,1,2,3]                     # time

# # # Plot function
# # #plt.plot(s,tem)

# fig, ax = plt.subplots()

# ax.fill(s, tem, zorder=5)

# # # Setting title 
# # plt.title(r'Temperature', fontsize=20)

# # # Set x and y labels
# # plt.xlabel('time')
# # plt.ylabel('temperature')


# # Show plot
# plt.show()


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

    def print_data(self,key):
        # This function is to print values in each list
        # Require enter self.print_data(key) in main function
        # In order to make this class to work, the key must be 
        # enter as tem, hum, lgt, pir
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
        else: 
            print("List not found")

    def print_all(self):
        # This function is to display all lists
        # Require to enter self.print_all() in main function
        print("Temperature data display:")
        print(self.tem_list)
        print("Humidity data display:")
        print(self.hum_list)
        print("Illuminance data display:")
        print(self.lgt_list)
        print("PIR sensor data display:")
        print(self.PIR_list)

if __name__ == "__main__":
    # testing
    d = Mapping('Bedroom')
    
    d.add_data('tem',23.1)
    d.add_data('tem',23.2)
    d.add_data('tem',23.2)
    d.add_data('tem',23.3)
    d.add_data('tem',23.1)
    d.add_data('tem',23.2)
    d.add_data('tem',23.2)
    
    d.add_data('hum',10)
    d.add_data('hum',10.1)
    d.add_data('hum',10.2)
    d.add_data('hum',10.2)
    d.add_data('hum',10.1)
    d.add_data('hum',10.3)
    
    d.add_data('lgt',100)
    d.add_data('lgt',100.1)
    d.add_data('lgt',100.2)
    d.add_data('lgt',100.2)
    d.add_data('lgt',100.1)
    d.add_data('lgt',100.3)
    
    d.add_data('pir',1)
    d.add_data('pir',1)
    d.add_data('pir',0)
    d.add_data('pir',0)
    d.add_data('pir',0)
    d.add_data('pir',1)

    d.print_all()