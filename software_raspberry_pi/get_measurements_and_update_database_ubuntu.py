import gpiozero # for GPIO pin control
import time # for database timestamp and LED blinking
import mysql.connector # for database updates
import threading # for running LED and temperature processes in the background


rain_sensor_gpio_pin = gpiozero.Button("BOARD18")
sampling_interval_time = 900 # measurements taken every 900 seconds (15 minutes)
volume_per_rainfall_bucket = 0.2794 # millimetres^3 per bucket tip. Refer to hardware datasheet.
rainfall_buckets_counted = 0
rainfall_volume_counted = 0
temperature_measurement_interval = 5 # seconds
temperature_list = []
average_temperature = 0


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
    global average_temperature
    weather_database = mysql.connector.connect(
        host="localhost",
        user="database_administrator",
        password="database_administrators_password",
        database="weather"
    )
    cursor = weather_database.cursor()
    # weather_measurements_table_last_row_identification = cursor.lastrowid

    timestamp_for_database = time.strftime('%Y-%m-%d %H:%M:%S')

    data_weather_element = {
        'AmbientTemperature': average_temperature,
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

    print("Rainfall volume: " + str(rainfall_volume_counted) + " mm^3")
    print("Ambient temperature: " + str(average_temperature) + "°C")
    print("\r")


def add_to_temperature_list():
    from smbus import SMBus
    bus = SMBus(1)
    while True:
        global temperature_list
        global temperature_measurement_interval
        upper_byte, lower_byte = bus.read_i2c_block_data(0x18, 0x05, 2)
        upper_byte = upper_byte & int("0x1F", 0)
        if ((upper_byte & int("0x10", 0)) == int("0x10", 0)):  # TA < 0°C
            upper_byte = upper_byte & int("0x0F", 0)       # Clear sign
            temperature_current = 256 - ((upper_byte * 16) + (lower_byte / 16))
        else:                              # TA ³ 0°C
            temperature_current = (upper_byte * 16) + (lower_byte / 16)
        temperature_list.append(temperature_current)
        time.sleep(1)


def update_average_of_temperature_list():
    global temperature_list
    global average_temperature
    average_temperature = sum(temperature_list) / len(temperature_list)


def reset_temperature_list():
    global temperature_list
    temperature_list = []


while True:
    threaded_led_blinking = threading.Thread(target=led_blink)
    threaded_led_blinking.start()

    threaded_temperature_measurement = threading.Thread(target=add_to_temperature_list)
    threaded_temperature_measurement.start()

    while True:
        start_time = time.time()
        while time.time() <= start_time + sampling_interval_time:
            rain_sensor_gpio_pin.when_pressed = rainfall_bucket_tipped
        
        update_average_of_temperature_list()

        add_to_database()
        
        reset_rainfall_buckets_counted()
        reset_rainfall_volume_counted()
        reset_temperature_list()
