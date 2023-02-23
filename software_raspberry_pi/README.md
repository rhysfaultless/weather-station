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


## Resources

- [ROS2 on Raspberri Pi](https://docs.ros.org/en/foxy/How-To-Guides/Installing-on-Raspberry-Pi.html)
- [Raspberry Pi Foundation](https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/)

## I tried, but found issues

- installing dependencies for [MariaDB Connector](https://mariadb.com/docs/skysql/connect/programming-languages/python/install/)
