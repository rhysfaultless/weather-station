import lgpio
from time import sleep

LED = 23 # pin_16 = gpio_23
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED)


while True:
    lgpio.gpio_write(h, LED, 1)
    sleep(1)
    lgpio.gpio_write(h, LED, 0)
    sleep(1)
    