import gpiozero
from time import sleep

led = gpiozero.LED("BOARD16")
button = gpiozero.Button("BOARD18")

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()
