#!usr/bin/python

#Git all necessary files

#Git Python3 and pip3
sudo apt-get install python3
sudo apt-get install python3-pip

#Git MCP3008 files
#Guide here:
#https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
print("git MCP3008 Adafruit library...")
sudo apt-get install build-essential python-dev python-smbus git
cd ~
git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
print("got MCP3008 Adafruit library!")

#Git Twython files
#Guide here:
#https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/work$
print("git Twython...")
sudo pip3 install twython
print("got Twython!")

#Git authentication and boot files
sudo git clone https://github.com/HOCProj/main/ RaspberryPi/auth.py
print("got auth.py!")
sudo git clone https://github.com/HOCProj/main/ RaspberryPi/boot.py
print("got boot.py!")

#Git WiringPi
sudo git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
print("got WiringPi!")

#Git AVRDude
print("*** THIS WILL PAUSE SEVERAL TIMES ***")
sudo apt-get install bison automake autoconf flex git gcc
sudo apt-get install gcc-avr binutils-avr avr-libc
git clone https://github.com/kcuzner/avrdude 
cd avrdude/avrdude
./bootstrap && ./configure && sudo make install
print("Got AVRDude!")

#Git ATTiny example scripts
print("Git ATTiny85 files...")
cd /home/pi
mkdir ATTiny85
cd ATTiny85
git clone https://github.com/HOCProj/ main/ ATTiny85
print("Got ATTiny85 files!")

#Git Telepot (Telegram library)
print("Git telepot...")
sudo pip install telepot
print("Got Telepot!")

#Git SSMTP (email)
print("Git SSMTP...")
sudo apt-get install ssmtp
sudo apt-get install mailutils
print("Got SSMTP!")
