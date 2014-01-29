#!/usr/bin/python
from time import sleep
import random

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
lcd = Adafruit_CharLCDPlate()

frequency = 8
delay = 12
duration = 5
responses = []

responses.append( "Hello?" )
responses.append( "Where are you?" )
responses.append( "What are you\nwearing?" )
responses.append( "Whatcha doing?" )
responses.append( "Can you hear me\nNOW?" )
responses.append( "Why are you here" )
responses.append( "Take a picture\n-- lasts longer")

sleep( delay )
def ask_glados():
	random_msg = random.randint( 0, len( responses ) - 1 )
	
	lcd.clear()
	lcd.backlight( lcd.WHITE )
        lcd.message( responses[random_msg] )
        sleep(duration)
	lcd.clear()
	#lcd.backlight( lcd.OFF )
	sleep(frequency)
	ask_glados()
ask_glados()
