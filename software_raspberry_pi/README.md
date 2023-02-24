# weather-station-ros2, Software

---

## Tools

- Git and GitHub
- VS Code
- [VS Code extension for Remote development](https://code.visualstudio.com/docs/remote/ssh)
- [Ubuntu Server 22.04](https://ubuntu.com/download/raspberry-pi) or Raspberry Pi OS (64-bit)
- [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
- [gpiozero](https://gpiozero.readthedocs.io/en/stable/index.html)
  - Install with `sudo apt install python3-gpiozero` ( Already installed on Raspberry Pi OS )
- [MySQL Connector](https://www.w3schools.com/python/python_mysql_getstarted.asp)
   ```
   pip3 install mysql-connector-python
   ```
- [MariaDB](https://mariadb.com/kb/en/installing-mariadb-deb-files/#installing-mariadb-packages-with-apt)
  ```
  sudo apt update
  sudo apt upgrade
  sudo apt-get install mariadb-server
  sudo apt-get install libmariadb3 libmariadb-dev
  ```
  The MySQL / MariaDB database will be running on boot.
  You can connect to it by entering `sudo mysql` into a terminal.

  NOTE: these MySQL commands require the `;` line ending syntax.

  - Then add a username and password for the database:
    ```
    create user database_administrator IDENTIFIED by 'database_administrators_password';
    ```
    - Change `database_administrator` to whatever username you would like.
    - Change `database_administrator_password` to whatever password you would like.
  - Grant privileges to all users:
    ```
    grant all privileges on *.* to 'database_administrator' with grant option;
    ```
    - Change `database_administrator` to whatever username you set earlier.
  - Create a database:
    ```
    create database weather;
    ```
    - This new database is named `weather`
  - Connect to the database:
    ```
    use weather;
    ```
    - The prompt will change to `MariaDB [weather]>`
    - The prompt was `MariaDB [(none)]>`
  - Create a table inside the `weather` database:
    ```
    CREATE TABLE WeatherMeasurements (
        ElementIdentification BIGINT NOT NULL AUTO_INCREMENT,
        AmbientTemperature DECIMAL(6,2) NOT NULL,
        RainfallVolume DECIMAL (6,2) NOT NULL,
        TimestampValue TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY ( ElementIdentification )
    );
    ```
    - This is a table named `WeatherMeasurements`.
      It has columns of:
      - `ElementIdentification`
      - `AmbientTemperature`
      - `RainfallVolumen`
      - `TimestampValue`
    - The `ElementIdentification` column is set as the primary key.
  - [Adafruit MCP9809 library](https://learn.adafruit.com/adafruit-mcp9808-precision-i2c-temperature-sensor-guide/python-circuitpython)
    ```
    sudo pip3 install adafruit-circuitpython-mcp9808
    ```
  - Configure the Raspberry Pi to use I2C devices, using either:
    - the GUI tool `Raspberry Pi Configuration` 
    - or the commant line tool `sudo raspi-config`


## Resources

- [ROS2 on Raspberri Pi](https://docs.ros.org/en/foxy/How-To-Guides/Installing-on-Raspberry-Pi.html)
- [Raspberry Pi Foundation](https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/)

## I tried, but found issues

- installing dependencies for [MariaDB Connector](https://mariadb.com/docs/skysql/connect/programming-languages/python/install/)

# Useful commands for MySQL

|| Command Type || Command                               || Purpose                                                             ||
| :------------ | :------------------------------------- | :------------------------------------------------------------------- |
| bash          | `sudo mysql;`                          | enters the MySQL terminal                                            |
| MySQL         | `use weather;`                         | connect to the `weather` database                                    |
| MySQL         | `show full tables;`                    | list all the tables inside the current database                      |
| MySQL         | `show columns in WeatherMeasurements;` | lists the columens in the table `WeatherMeasurements`                |
| MySQL         | `select * from WeatherMeasurements;`   | lists all rows and related data from the table `WeatherMeasurements` |
| MySQL         | `delete from WeatherMeasurements;`     | deletes all rows from the table `WeatherMeasurements`                |

# TODO hardware to purchase

|| Quantity || Description               || Manufacturer || Item Number || DigiKey                                                                                       ||
| :-------- | :------------------------- | :------------ | :----------- | :--------------------------------------------------------------------------------------------- |
| 1         | Breadboard                 | Adafruit      | 2310         | [1528-1369-ND](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/2310/5629417) |
| 2         | 0.1" header, female, 1 X 6 | Adam Tech     | RS1-06-G     | [2057-RS1-06-G-ND](https://www.digikey.ca/en/products/detail/adam-tech/RS1-06-G/9832050)       | 
| 1         | Terminal (RJ12)            | Adam Tech     | MTJ-661X1    | [2057-MTJ-661X1-ND](https://www.digikey.ca/en/products/detail/adam-tech/MTJ-661X1/9832264)     |
