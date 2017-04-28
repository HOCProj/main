**HOC Project**

*Hutchins-O'Dell-Cooper Senior Design Project Repository*

This project uses the following libraries:

Adafruit MCP3008 library:
https://github.com/adafruit/Adafruit_Python_MCP3008

Twython AND Oauth:
https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/requirements/software/
https://www.raspberrypi.org/forums/viewtopic.php?t=162900&p=1054189

AVRDude:
http://www.raspihub.com/go/4c3370e8431b091c1698106135127581a646f3e2829fc26123d2bbfb34199dfa

SSMPT (Send email):
http://stackoverflow.com/questions/38391412/raspberry-pi-send-mail-from-command-line-using-gmail-smtp-server

mailutils

Fetchmail (Receive email):
http://www.raspberry-projects.com/pi/software_utilities/email/fetchmail-to-receive-email

chmod 755 and chown

Schedule tasks:
https://www.raspberrypi.org/documentation/linux/usage/cron.md

These libraries will be automatically downloaded and installed by executing the GitAll.py file.

**User Manual**

Setup guides and example scripts are available in the appropriate folders (Raspberry Pi and ATTiny85).

The primary purpose of our project is to provide a cheap means of extending the capabilities of the Raspberry Pi and the ATTiny85. We also have the secondary purpose of compiling all of the necessary software and troubleshooting into one location, so that a person with beginner-intermediate level experience with circuitry and code can avoid the wiring mess of traditional electronics and the days or weeks of research into software.

On the board is a 40-pin header. This is used to connect our project to the Raspberry Pi. Doing so gives the Pi access to an MCP3008 ADC and an external power supply. There is also an 8-pin socket for an ATTiny85, which can be connected and interfaced with the IR receiver and the external power supply and ADC as well. The Raspberry Pi and ATTiny85 can be used simultaneously or separately. If using both of them and the ADC for either (cannot be used by both at one time), you must be mindful of shared connections. Refer to the board schematics.

A green screw block connector is situated next to the IR receiver. This can be used to receive external power (up to 33V and 3A continuous), and regulate it to ~5V for the Pi and ATTiny. Next to that is an 8-pin straight header. These are the analog inputs for the ADC, corresponding to channels 0-7. Next to that is a 2x4-pin header, which is laid out exactly the same as the ATTiny85 pins and is used to access those pins. Below that is a button which resets the ATTiny85 (pulls the RESET pin to ground).

There are two 2-pin headers, each labeled RPi and MCP. These are used to connect and disconnect power to the Raspberry Pi and MCP3008 respectively. If, for example, you want the ATTiny and Raspberry Pi to communicate over the ISP lines, the MCP header should be disconnected to prevent that chip from interfering with the signals. Or if you want the ATTiny to use the ADC and the Pi is not in use or powered separately, the RPi header should be disconnected.]
