import mysql.connector # for database updates

weather_database = mysql.connector.connect(
    host="localhost",
    user="database_administrator",
    password="database_administrator_password",
    database="weather"
)

cursor = weather_database.cursor()
sql_statement = "select * from WeatherMeasurements order by ElementIdentification desc;"
cursor.execute(sql_statement)
output = cursor.fetchall()
previous_element = ()
for row_in_table in output:
    print("Element Identification: " + str(row_in_table[0]))
    print("Temperature:            " + str(row_in_table[1]))
    print("Rainfall Volume:        " + str(row_in_table[2]))
    print("Timestamp:              " + str(row_in_table[3]))
#    if row_in_table[0] > 10:
#        print("Time difference:        " + str(row_in_table[3] - previous_element[3]))
    print("\r")
    previous_element = row_in_table
