import gpiozero
import time
import status_led # to blink when this program is running

rain_sensor_gpio_pin = gpiozero.Button("BOARD18")
sampling_interval_time = 10 # measurements taken every 10 seconds
volume_per_rainfall_bucket = 0.2794 # millimetres^3 per bucket tip. Refer to hardware datasheet.
rainfall_buckets_counted = 0
rainfall_volume_counted = 0


def rainfall_bucket_tipped():
    global rainfall_buckets_counted
    global rainfall_volume_counted
    rainfall_buckets_counted += 1
    rainfall_volume_counted = rainfall_buckets_counted * volume_per_rainfall_bucket


def reset_rainfall_buckets_counted():
    global rainfall_buckets_counted
    rainfall_buckets_counted = 0


def reset_rainfall_volume_counted():
    global rainfall_volume_counted
    rainfall_volume_counted = 0


while True:
    start_time = time.time()

    while time.time() <= start_time + sampling_interval_time:
        rain_sensor_gpio_pin.when_pressed = rainfall_bucket_tipped

    reset_rainfall_buckets_counted()
    reset_rainfall_volume_counted()
