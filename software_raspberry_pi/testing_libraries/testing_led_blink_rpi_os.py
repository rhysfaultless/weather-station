import gpiozero
from time import sleep

led = gpiozero.LED("BOARD16")

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    