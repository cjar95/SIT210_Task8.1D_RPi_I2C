#Import the necessary libraries
import smbus
import time

#Set the 12C defined constants
AmbientSensor = 0x23 # Default device I2C address
PowerOff = 0x00 # No active state
PowerOn = 0x01 # Power on
Reset = 0x07 # Reset data register value

#We will operate in high res mode
ONE_TIME_HIGH_RES_MODE = 0x20

#Sets up the I2C interface
bus = smbus.SMBus(1)

#Method converts data into a decimal number
def ConvertToDecimal(data):
    result = (data[1] + (256 * data[0])) / 1.2
    return (result)

#Method to read data from the BH1750 via the I2C interface
def ReadLight(addr = AmbientSensor):
    data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
    return ConvertToDecimal(data)

#Main drives the program
def main():
    while True:
        #New variable that calls ReadLight()
        LightLevel = ReadLight()
        #Prints the current Light Level
        print(LightLevel)
        
        #Conditions that determine the lights respective category
        if(LightLevel <10):
            print("Light level is too Dark!!")
        if(LightLevel >10 and LightLevel <30):
            print("Light level is Dark")
        if(LightLevel >30 and LightLevel <50):
            print("Light level is Medium")
        if(LightLevel >50 and LightLevel <70):
            print("Light level is Bright")
        elif(LightLevel >70):
            print("Light level is too Bright!!")

        time.sleep(1)
main()
