#!/usr/bin/python

import argparse
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

colors = {
        'red'    : lcd.RED,
	'yellow' : lcd.YELLOW,
       	'green'  : lcd.GREEN,
	'teal'   : lcd.TEAL,
	'blue'   : lcd.BLUE,
	'violet' : lcd.VIOLET,
	'white'  : lcd.WHITE,
	'on'	 : lcd.ON,
	'off'    : lcd.OFF
}


# Initialize the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("m", help="The message to display on the LCD")
parser.add_argument("c", type=str, help="BLUE, RED")
args = parser.parse_args()

# Assign variables
message = args.m
color = colors[args.c]

# Clear display and show greeting, pause 1 sec
lcd.clear()
lcd.message(message)
lcd.backlight(color)
