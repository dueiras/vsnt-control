# VSNT Control (AVP-MOOS)

In portuguese VSNT stands for Autonomous Surface Vehicle (ASV). VSNT Control is GUI made with `tkinter` using `MOOS-IvP` for controlling remotely and autonomously a LAB-Vessel.

![GUI demo](https://github.com/dueiras/vsnt-control/blob/master/images/gui_demo.png?raw=true)

The interface allows:
-> Remote control of Gear, Thrust and Rudder
-> Autonomous navigation using Moos-IvP
-> Access Cameras and Sonar images
-> View other ships in the Map using AIS messages
-> Interface for tunning a PID controller

This code was used as a GUI for our main Moos application moos-ivp-vsnt.

## Run the code

```console
user@computer:~$ python3 main.py
```
