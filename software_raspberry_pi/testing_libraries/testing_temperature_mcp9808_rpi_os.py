from time import sleep
import board
import busio
import adafruit_mcp9808
i2c = busio.I2C(board.SCL, board.SDA)
mcp = adafruit_mcp9808.MCP9808(i2c)

while True:
    print('Temperature: {} degrees C'.format(mcp.temperature))
    sleep(3)
