#!/usr/bin/python

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
lcd = Adafruit_CharLCDPlate()

import time
from datetime import datetime
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def procedure(ip):
	now = time.strftime("%c")
	frequency = 5	

	lcd.clear();
	lcd.message( now + "\n  " + ip )
	lcd.backlight(lcd.TEAL)
	time.sleep(frequency)
	procedure(ip)

ip = get_ip_address('wlan0');
#ip = "Acquiring IP..."
# Clear display and show greeting, pause 1 sec
lcd.clear()
procedure(ip)
