# Pinout between Arduino UNO R3 and Pico W
# GRD - GRD
# VIN - VBUS
# SCL - GP9
# SDA - GP8

import board
import busio

from adafruit_bus_device.i2c_device import I2CDevice


# Sets the I2C address
I2C_ADDR = 0x05
# Initialize the I2C bus
i2c = busio.I2C(scl=board.GP9, sda=board.GP8, frequency=10000)
# Create an I2C device
i2c_device = I2CDevice(i2c , I2C_ADDR)

print(i2c)
print("Initializing I2C as Master")

while True:
    print("Enter 1 for ON or 0 for OFF")
    ledstate = input(">>>>  ")
    if ledstate == "1":
        with i2c_device:
            i2c_device.write(bytes([0x1]))   # switch it on
            print("LED is ON")
    elif ledstate == "0":
        with i2c_device:
            i2c_device.write(bytes([0x0]))   # switch it off
            print("LED is OFF")
    else:
        print("invalid input, goodbye!")
        break   # Exit the loop if input is not 1 or 0


