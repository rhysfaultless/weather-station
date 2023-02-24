import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="database_administrator",
  password="database_administrator_password",
  database="weather",
)

print(mydb)
