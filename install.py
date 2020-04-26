#!/usr/bin/env python
# -*- coding: utf-8 -*-

#[*] Name of the Tool: GeoTrackerIP
#[*] Description: "Geolocalize IP Public"
#[*] Installer of the Tool: GeoTrackerIP
#[*] Author: JRIC2002
#[*] Date: 15/03/2019

#MODULES

#External Modules
import itertools
import time
import os
import sys

#Internal Modules
from modules.logo import geotrackerip_logo

#ANSI COLORS

#Foreground
black = "\033[1;30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m" 
blue = "\033[1;34m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"

#Background
b_black = "\033[1;40m"
b_red = "\033[1;41m"
b_green = "\033[1;42m"
b_yellow = "\033[1;43m"
b_blue = "\033[1;44m"
b_magenta = "\033[1;45m"
b_cyan = "\033[1;46m"
b_white = "\033[1;47m"

#CLEAN CONSOLE
def clean():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    else:
        break
        
#PROCESS OF INSTALLING
def install():
    bucle = itertools.cycle("/-|-\|")
    for i in range(30):
        print("{}[{}*{}] {}Installing Modules...{}{}".format(cyan, white, cyan, green, next(bucle), white), end='\r')
        time.sleep(0.1) 
    print("")
    print("")
    os.system("python3 -m pip install requests")
    print("")
    print("                     {}>> Installation Complete <<{}".format(blue, white))
    print("")
    time.sleep(1)

#START
clean()
geotrackerip_logo.logo()
install()
