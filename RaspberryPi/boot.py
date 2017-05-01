#!usr/bin/python
print("Boot script started")

import random
import datetime
import os
import socket
from twython import Twython

print("Twython imported successfully.")
#auth.py is a copy of auth.py in /home/pi/twitter
from auth import (
        conKey,
        conSec,
        accTok,
        accSec
)
print("API info imported successfully.")

n = random.uniform(0,10)
t = datetime.datetime.now()
tweetStr = t.strftime('%m/%d/%Y %H:%M:%S ') + str(n)

print("Tweet is " + tweetStr)
print("Sending boot tweet...")
api=Twython(conKey,conSec,accTok,accSec)
api.update_status(status=tweetStr)
print("Boot tweet sent successfully")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

ip = get_ip()
target=open("ipaddress.txt",'w')
target.truncate()
target.write(ip)
target.close()
print("calling emailip script...")
os.system("bash emailip")
