import gpiozero
import time
import mysql.connector
import threading

rain_sensor_gpio_pin = gpiozero.Button("BOARD18")
sampling_interval_time = 10 # measurements taken every 10 seconds
volume_per_rainfall_bucket = 0.2794 # millimetres^3 per bucket tip. Refer to hardware datasheet.
rainfall_buckets_counted = 0
rainfall_volume_counted = 0
ambient_temperature = 0  # Using zero as a placeholder, until adding functions for temperature sensor MCP9808


def led_blink():
    led_gpio_pin = gpiozero.LED("BOARD16")
    led_blinking_interval_on = 0.6
    led_blinking_interval_off = 5
    while True:
        led_gpio_pin.on()
        time.sleep(led_blinking_interval_on)
        led_gpio_pin.off()
        time.sleep(led_blinking_interval_off)


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


def add_to_database():
    global rainfall_volume_counted
    global ambient_temperature
    weather_database = mysql.connector.connect(
        host="localhost",
        user="database_administrator",
        password="database_administrator_password",
        database="weather"
    )
    cursor = weather_database.cursor()
    # weather_measurements_table_last_row_identification = cursor.lastrowid

    timestamp_for_database = time.strftime('%Y-%m-%d %H:%M:%S')

    data_weather_element = {
        'AmbientTemperature': ambient_temperature,
        'RainfallVolume': rainfall_volume_counted,
        'TimestampValue': timestamp_for_database
    }

    add_weather_element = ("INSERT INTO WeatherMeasurements "
              "(AmbientTemperature, RainfallVolume, TimestampValue) "
              "VALUES (%(AmbientTemperature)s, %(RainfallVolume)s, %(TimestampValue)s)")

    # ElementIdentification is not included in data_weather_element or add_weather_element
    # This is because the table, WeatherMeasurements is configured to AutoIncrement this element

    cursor.execute(add_weather_element, data_weather_element)
    weather_database.commit()
    cursor.close()
    weather_database.close()

    print(str(rainfall_volume_counted))

    reset_rainfall_buckets_counted()
    reset_rainfall_volume_counted()


while True:
    threaded_led_blinking = threading.Thread(target=led_blink)
    threaded_led_blinking.start()
    while True:
        start_time = time.time()
        while time.time() <= start_time + sampling_interval_time:
            rain_sensor_gpio_pin.when_pressed = rainfall_bucket_tipped
        add_to_database()
