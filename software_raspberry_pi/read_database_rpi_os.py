import datetime
import mysql.connector # for database updates


# Connect to the database
weather_database = mysql.connector.connect(
    host="localhost",
    user="database_administrator",
    password="database_administrator_password",
    database="weather"
)


# Pull the latest 672 rows of data from the database table WeatherMeasurements
cursor = weather_database.cursor()
sql_statement = "select * from WeatherMeasurements order by ElementIdentification desc limit 672;"
cursor.execute(sql_statement)
database_rows = cursor.fetchall()


# The current time difference should be less than 900 seconds, since this is the intended database update interval
current_time = datetime.datetime.now()
latest_database_time = database_rows[0][3]
current_time_difference = (current_time - latest_database_time).total_seconds()


# Only structure the data if a row was added to the database within the last 15 minutes
if current_time_difference > (900 * 1.1):
    print("The database has not updated in the past 15 minutes")
else:
    # Messages are being added to the database in ~15 minute intervals

    interval_additional_buffer           = 10 # seconds
    seconds_to_remove                    = 900


    expected_number_rows_15_minutes      = 1
    interval_15_minutes                  = 900 - seconds_to_remove + interval_additional_buffer # seconds
    database_temperature_list_15_minutes = []
    average_temperature_15_minutes       = None
    database_rainfall_list_15_minutes    = []
    total_rainfall_15_minutes          = None

    expected_number_rows_1_hour          = 4
    interval_1_hour                      = 3600 - seconds_to_remove + interval_additional_buffer # seconds
    database_temperature_list_1_hour     = [] #   4 rows   #   3600 seconds
    average_temperature_1_hour           = None
    database_rainfall_list_1_hour        = []
    total_rainfall_1_hour              = None

    expected_number_rows_1_day           = 96
    interval_1_day                       =  86400 - seconds_to_remove + interval_additional_buffer # seconds
    database_temperature_list_1_day      = [] #  96 rows   #  86400 seconds
    average_temperature_1_day            = None
    database_rainfall_list_1_day         = []
    total_rainfall_1_day               = None

    expected_number_rows_2_days          = 192
    interval_2_days                      = 172800 - seconds_to_remove + interval_additional_buffer # seconds
    database_temperature_list_2_days     = [] # 192 rows   # 172800 seconds
    average_temperature_2_days           = None
    database_rainfall_list_2_days        = []
    total_rainfall_2_days              = None

    expected_number_rows_3_days          = 288
    interval_3_days                      = 259200 - seconds_to_remove + interval_additional_buffer # seconds
    database_temperature_list_3_days     = [] # 288 rows   # 259200 seconds
    average_temperature_3_days           = None
    database_rainfall_list_3_days        = []
    total_rainfall_3_days              = None

    expected_number_rows_7_days          = 672
    interval_7_days                      = 604800 - seconds_to_remove + interval_additional_buffer # seconds
    database_temperature_list_7_days     = [] # 672 rows   # 604800 seconds
    average_temperature_7_days           = None
    database_rainfall_list_7_days        = []
    total_rainfall_7_days              = None


    # Check the times for each row, and only add the append a list it the row's timestamp is within the accepted range.
    # This is checking for database lapses / outages
    for database_row in database_rows:
        database_row_time_difference = (latest_database_time - database_row[3]).total_seconds()
        if database_row_time_difference > interval_7_days:
            print("Error: This row of the database is older than the 7 day interval")
            break
        
        elif (database_row_time_difference <= interval_7_days):
            database_temperature_list_7_days.append(database_row[1])
            database_rainfall_list_7_days.append(database_row[2])
            
            if (database_row_time_difference <= interval_3_days):
                database_temperature_list_3_days.append(database_row[1])
                database_rainfall_list_3_days.append(database_row[2])
                
                if (database_row_time_difference <= interval_2_days):
                    database_temperature_list_2_days.append(database_row[1])
                    database_rainfall_list_2_days.append(database_row[2])
                    
                    if (database_row_time_difference <= interval_1_day):
                        database_temperature_list_1_day.append(database_row[1])
                        database_rainfall_list_1_day.append(database_row[2])
                        
                        if (database_row_time_difference <= interval_1_hour):
                            database_temperature_list_1_hour.append(database_row[1])
                            database_rainfall_list_1_hour.append(database_row[2])
                            
                            if (database_row_time_difference <= interval_15_minutes):
                                database_temperature_list_15_minutes.append(database_row[1])
                                database_rainfall_list_15_minutes.append(database_row[2])


    # Calculate the average temperatures and rainfall volumes using the compiled lists
    if len(database_temperature_list_15_minutes) >= (expected_number_rows_15_minutes - 1):
        average_temperature_15_minutes = sum(database_temperature_list_15_minutes) / len(database_temperature_list_15_minutes)
        total_rainfall_15_minutes = sum(database_rainfall_list_15_minutes) / len(database_rainfall_list_15_minutes)

        if len(database_temperature_list_1_hour) >= (expected_number_rows_1_hour - 1):
            average_temperature_1_hour = sum(database_temperature_list_1_hour) / len(database_temperature_list_1_hour)
            total_rainfall_1_hour = sum(database_rainfall_list_1_hour) / len(database_rainfall_list_1_hour)
        
            if len(database_temperature_list_1_day) >= (expected_number_rows_1_day - 1):
                average_temperature_1_day = sum(database_temperature_list_1_day) / len(database_temperature_list_1_day)
                total_rainfall_1_day = sum(database_rainfall_list_1_day) / len(database_rainfall_list_1_day)
        
                if len(database_temperature_list_2_days) >= (expected_number_rows_2_days - 1):
                    average_temperature_2_days = sum(database_temperature_list_2_days) / len(database_temperature_list_2_days)
                    total_rainfall_2_days = sum(database_rainfall_list_2_days) / len(database_rainfall_list_2_days)

                    if len(database_temperature_list_3_days) >= (expected_number_rows_3_days - 1):
                        average_temperature_3_days = sum(database_temperature_list_3_days) / len(database_temperature_list_3_days)
                        total_rainfall_3_days = sum(database_rainfall_list_3_days) / len(database_rainfall_list_3_days)

                        if len(database_temperature_list_7_days) >= (expected_number_rows_7_days - 1):
                            average_temperature_7_days = sum(database_temperature_list_7_days) / len(database_temperature_list_7_days)
                            total_rainfall_7_days = sum(database_rainfall_list_7_days) / len(database_rainfall_list_7_days)
                        else:
                            print("\r")
                            print("Error: There are no measurements within the last 7 days.")
                    else:
                        print("\r")
                        print("Error: There are no measurements within the last 3 days.")
                else:
                    print("\r")
                    print("Error: There are no measurements within the last 2 days.")
            else:
                print("\r")
                print("Error: There are no measurements within the last 1 day.")
        else:
            print("\r")
            print("Error: There are no measurements within the last 1 hour.")
    else:
        print("\r")
        print("Error: There are no measurements within the last 15 minutes.")

    # Printing the calcumated averages / totals
    print("\r")
    print("average_temperature_15_minutes: " + str(average_temperature_15_minutes))
    print("total_rainfall_15_minutes:      " + str(total_rainfall_15_minutes))
    print("\r")
    print("average_temperature_1_hour:     " + str(average_temperature_1_hour))
    print("total_rainfall_1_hour:          " + str(total_rainfall_1_hour))
    print("\r")
    print("average_temperature_1_day:      " + str(average_temperature_1_day))
    print("total_rainfall_1_day:           " + str(total_rainfall_1_day))
    print("\r")
    print("average_temperature_2_days:     " + str(average_temperature_2_days))
    print("total_rainfall_2_days:          " + str(total_rainfall_2_days))
    print("\r")
    print("average_temperature_3_days:     " + str(average_temperature_3_days))
    print("total_rainfall_3_days:          " + str(total_rainfall_3_days))
    print("\r")
    print("average_temperature_7_days:     " + str(average_temperature_7_days))
    print("total_rainfall_7_days:          " + str(total_rainfall_7_days))
    print("\r")
