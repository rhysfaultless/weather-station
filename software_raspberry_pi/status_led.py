import gpiozero
from time import sleep

led_gpio_pin = gpiozero.LED("BOARD16")
blinking_interval_on = 0.6
blinking_interval_off = 5

while True:
    led_gpio_pin.on()
    sleep(blinking_interval_on)
    led_gpio_pin.off()
    sleep(blinking_interval_off)
