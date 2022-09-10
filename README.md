# weather-station-ros2

---

## Purpose and background

I want a rainfall and termperature tracking system for my home.
I would also like to have this data as ROS topics to use for later automation projects.
There are several tutorials and projects detailing similar setups, but none that then convert the data into ROS.

## References

- [Hardware ideas](https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/5) from a Raspberry Pi tutorial.
- [Hardware ideas](https://learn.sparkfun.com/tutorials/weather-meter-hookup-guide/all) from a Sparkfun tutorial.
- [micro-ROS supported hardware](https://micro.ros.org/docs/overview/hardware/) instead of using a computer like a Raspberry Pi.

## Install Prettier for text formatting of README files

1.  Clone the repository
2.  Open a terminal shell to the cloned repository
3.  Make sure you have Node.js installed by running `node -v`.
    Download and install [Node.js](https://nodejs.org/).
4.  In the terminal, run `npm install`.
    This will install the dependencies listed in the file _package.json_.
5.  From now on you can just run `npx prettier --write <filepath>` to format a file.
    For example; to format the README in the electrical folder:
    ```
    npx prettier --write electrical/README.md
    ```
    This will format the file according to the rules listed in the file _.prettierrc.json_.
    You will not need to run through the other steps again.
