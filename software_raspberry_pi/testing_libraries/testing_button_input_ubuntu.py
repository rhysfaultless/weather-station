import lgpio
from time import sleep

h = lgpio.gpiochip_open(0)
LED = 23 # pin_16 = gpio_23
BUTTON = 24 # pin_18 = gpio_24

while True:
    if lgpio.gpio_read(h, BUTTON) == 0:
        lgpio.gpio_write(h, LED, 1)
    else:
        lgpio.gpio_write(h, LED, 0)
