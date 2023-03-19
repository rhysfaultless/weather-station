# pyton3 program to read a Microchip MCP9808 temperature sensor using I2C
# conversion equation explained on page 25 of the datasheet
from time import sleep
from smbus import SMBus

bus = SMBus(1)

while True:
    upper_byte, lower_byte = bus.read_i2c_block_data(0x18, 0x05, 2)

    upper_byte = upper_byte & int("0x1F", 0)
    if ((upper_byte & int("0x10", 0)) == int("0x10", 0)):  # TA < 0°C
        print('passed if check')
        print(upper_byte)
        upper_byte = upper_byte & int("0x0F", 0)       # Clear sign
        print(upper_byte)
        temperature = 256 - ((upper_byte * 16) + (lower_byte / 16))
    else:                              # TA ³ 0°C
        print('went to else')
        temperature = (upper_byte * 16) + (lower_byte / 16)
    print("resulting temperature")
    print(temperature)
    print("\r")
    sleep(1)
