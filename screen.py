#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13bc
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13bc Demo")

    epd = epd2in13bc.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)

    logging.info("Writing text")    
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    
    Blackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    Rimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image  

    drawblack = ImageDraw.Draw(Blackimage)
    drawr = ImageDraw.Draw(Rimage)

    drawblack.text((10, 0), 'Hello there!', font = font20, fill = 0)
    drawblack.text((10, 60), 'Using python3', font = font20, fill = 0)    
    drawr.text((10, 20), 'This is a test', font = font20, fill = 0)

    epd.display(epd.getbuffer(Blackimage), epd.getbuffer(Rimage))
    time.sleep(2)
    
    logging.info("Drawing BMP files")
    Blackimage = Image.open(os.path.join(picdir, 'black.bmp'))
    Rimage = Image.open(os.path.join(picdir, 'red.bmp'))

    epd.display(epd.getbuffer(Blackimage), epd.getbuffer(Rimage))
    time.sleep(2)
    
    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13bc.epdconfig.module_exit()
    exit()
