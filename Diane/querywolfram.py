#!/usr/bin/python

import wolframalpha
import sys

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

# Clear display and show greeting, pause 1 sec
lcd.clear()
lcd.backlight(lcd.WHITE)
lcd.message("Searching...")

# Get a free API key here http://products.wolframalpha.com/api/
# This is a fake ID, go and get your own, instructions on my blog.
app_id='EAL55P-UYQLAH8HJ7'

client = wolframalpha.Client(app_id)

query = ' '.join(sys.argv[1:])
res = client.query(query)

lcd.clear();
if len(res.pods) > 0:
    texts = ""
    pod = res.pods[1]
    if pod.text:
        texts = pod.text
    else:
        texts = "I have no answer for that"
    # to skip ascii character in case of error
    texts = texts.encode('ascii', 'ignore')
    print texts
    lcd.backlight(lcd.GREEN)
    lcd.message(texts)
else:
    print "Don't be such a bother."
    lcd.backlight(lcd.RED)
    lcd.message("Piss off!")

#sleep(5)
#lcd.clear()
#lcd.backlight(lcd.OFF)
