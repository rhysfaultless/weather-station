# weather-station-ros2, Software

---

## Tools

- Git and GitHub
- VS Code
- [VS Code extension for Remote development](https://code.visualstudio.com/docs/remote/ssh)
- [Ubuntu Server 22.04](https://ubuntu.com/download/raspberry-pi)
- [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
- [gpiozero](https://gpiozero.readthedocs.io/en/stable/index.html)
  - Install with `sudo apt install python3-gpiozero`

## Resources

- [ROS2 on Raspberri Pi](https://docs.ros.org/en/foxy/How-To-Guides/Installing-on-Raspberry-Pi.html)
- [Raspberry Pi Foundation](https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/)

## I tried, but found issues

- installing dependencies for [MariaDB Connector](https://mariadb.com/docs/skysql/connect/programming-languages/python/install/)

# Useful commands for MySQL

| Command Type | Command                                | Purpose                                                              |
| :----------- | :------------------------------------- | :------------------------------------------------------------------- |
| bash         | `sudo mysql;`                          | enters the MySQL terminal                                            |
| MySQL        | `use weather;`                         | connect to the `weather` database                                    |
| MySQL        | `show full tables;`                    | list all the tables inside the current database                      |
| MySQL        | `show columns in WeatherMeasurements;` | lists the columens in the table `WeatherMeasurements`                |
| MySQL        | `select * from WeatherMeasurements;`   | lists all rows and related data from the table `WeatherMeasurements` |
| MySQL        | `delete from WeatherMeasurements;`     | deletes all rows from the table `WeatherMeasurements`                |

# TODO hardware to purchase

| Quantity  | Description                | Manufacturer | Item Number | DigiKey                                                                                        |
| :-------- | :------------------------- | :----------- | :---------- | :--------------------------------------------------------------------------------------------- |
| 1         | Breadboard                 | Adafruit     | 2310        | [1528-1369-ND](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/2310/5629417) |
| 2         | 0.1" header, female, 1 X 6 | Adam Tech    | RS1-06-G    | [2057-RS1-06-G-ND](https://www.digikey.ca/en/products/detail/adam-tech/RS1-06-G/9832050)       | 
| 1         | Terminal (RJ12)            | Adam Tech    | MTJ-661X1   | [2057-MTJ-661X1-ND](https://www.digikey.ca/en/products/detail/adam-tech/MTJ-661X1/9832264)     |

# Installation

1.  Insert a micro-SD card in another computer, and open Raspberry Pi Imager (tested with v1.7.3).
    - Select the card from the devices
    - Select the OS as `Ubuntu Desktop 22.04.2 LTS, 64 bit`
    - click Write
2.  Once completed, insert the micro-SD into the Raspberry Pi, connect the Pi to Ethernet, and then turn the Pi on.
3.  Ubuntu installation and setup:
    - Location (_Toronto_)
    - Keyboard input (_US English_)
    - Hostname (_rp-001_)
    - Username (_administrator_)
    - Password (_****_)
    - The Pi will reboot, and then ask you to login
    - Skip the Google / Microsoft / Ubuntu login
    - Skip the Ubuntu Pro option
    - Choose whether to send system information to Canonical (_No_)
    - Choose whether to allow location services (_Yes_)
    - Select Done
4.  Optional, connect to a Wi-Fi network, or continue to use the hardwired network.    
5.  Update the system by opening a terminal, and running:
    ```
    sudo apt update
    sudo apt upgrade
    ```
6.  Install VS Code:
    - Open Firefox
    - Go to https://code.visualstudio.com/download
    - Download the _.deb_ for Ubuntu ARM64 (_v1.75.1_)
    - Once downloaded, double-click the file and open it with Software Installer
    - Allow it to install
    - Delete the _.deb_ from _~/Downloads_
7.  Install and configure Git by opening a terminal, and running:
    ```
    sudo apt install git
    git --version
    git config --global user.name <your user name here, without angle braces>
    git config --global user.email <your email here, without angle braces>
    ```
8.  Configure VS Code
    - Open VS Code
    - Open the Extensions panel on the left
    - Install _Git Graph_
    - Install _GitLens_
    - Install _Python_
9.  Clone this repository:
    - In the VS Code terminal:
      ```
      cd ~/Documents
      git clone https://github.com/rhysfaultless/weather-station-ros2.git
      ```

      Note: VS Code will request permission to access GitHub it this is the first use of GitHub + VS Code
    - File → Open Folder ...
    - Navigate to _~/Documents/weather-station-ros2.git_ and select _Open_
10. Install libraries and tools related to this repository, by running these lines in a terminal:
    1.  Python's pip3
        ```
        sudo apt install python3-pip
        sudo pip3 install --upgrade setuptools
        ```
    2.  [gpiozero](https://gpiozero.readthedocs.io/en/stable/index.html)
        ```
        sudo apt install python3-gpiozero
        ```
        - NOTE: this reqquires the _lgpio_ library to map cammands to the physical hardware pins.
    3.  [lgpio](https://ubuntu.com/tutorials/gpio-on-raspberry-pi#1-overview)
        ```
        sudo apt install python3-lgpio
        ```
        - [Manual from Ubuntu](https://manpages.ubuntu.com/manpages/jammy/man3/lgpio.3.html)
        - [Manual from PyPi](http://abyz.me.uk/lg/py_lgpio.html)
    4.  Give the _administrtor_ user permissions for the GPIO pins, and restart the Raspberry Pi
        ```
        sudo add user administrator dialout
        sudo reboot
        ```
    5.  [MySQL Connector](https://www.w3schools.com/python/python_mysql_getstarted.asp)
        ```
        pip3 install mysql-connector-python
        ```
    6.  [Adafruit MCP9808 library](https://learn.adafruit.com/adafruit-mcp9808-precision-i2c-temperature-sensor-guide/python-circuitpython)
        ```
        sudo pip3 install adafruit-circuitpython-mcp9808
        ```
    7.  Configure the Raspberry Pi's I2C pins using the [Raspberry Pi Configuration Tool](https://www.raspberrypi.com/documentation/computers/configuration.html)
        ```
        sudo apt-get install raspi-config
        sudo raspi-config
        ```
        - Select _Interfacing Options_
        - Select _I2C_
        - Select _Yes_
        - Select _Ok_
        - Select _Finish_
        ```
        sudo apt-get install -y python3-smbus
        sudo apt-get install -y i2c-tools
        ```
        - Test with `sudo i2cdetect -y 1`
    8.  [Adafruit's CircuitPython](https://learn.adafruit.com/building-circuitpython/linux)
        ```
        sudo add-apt-repository ppa:pybricks/ppa
        sudo apt install git gettext uncrustify cmake
        ```
    9.  [MariaDB](https://mariadb.com/kb/en/installing-mariadb-deb-files/#installing-mariadb-packages-with-apt)
        ```
        sudo apt-get install mariadb-server libmariadb3 libmariadb-dev
        ```

        -   NOTE: the MySQL / MariaDB database will be running on boot.
            You can connect to it by entering `sudo mysql` into a terminal.
        -   NOTE: SQL commands require the ; line ending syntax.
            This allows you to type multi-line commands before executing them.
        1.  `sudo mysql`
        2.  Then add a username and password:
            ```
            create user database_administrator identified by 'database_administrators_password';
            ```
            - Change `database_administrator` to whatever username you would like.
            - Change `database_administrator_password` to whatever password you would like.

        3.  Grant privileges to all users:
            ```
            grant all privileges on *.* to 'database_administrator' with grant option;
            ```
            - Change `database_administrator` to whatever username you set earlier.
        4.  Create a database:
            ```
            create database weather;
            ```
            - This new database is named `weather`
        5.  Connect to the database:
            ```
            use weather;
            ```
            - The prompt will change to `MariaDB [weather]>`
            - The prompt was `MariaDB [(none)]>`
        6.  Create a table inside the `weather` database:
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
        7.  Confirm that the table and columns were configured:
            ```
            show columns in WeatherMeasurements;
            ```
