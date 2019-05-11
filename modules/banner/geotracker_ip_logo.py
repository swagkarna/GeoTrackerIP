#/usr/bin/env python
# -*- coding: utf-8 -*-

# [*] Name of the Tool: GeoTrackerIP
# [*] Description: "Geolocalize IP Public"
# [*] Author: JRIC2002
# [*] Date: 15/03/2019

#IMPORTACION DE MODULOS

from colorama import init, Fore, Back, Style

#COLORS

#Foreground

black = Fore.BLACK
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW
white = Fore.WHITE
cyan = Fore.CYAN
magenta = Fore.MAGENTA

#Background

b_black = Back.BLACK
b_green = Back.GREEN
b_red = Back.RED
b_blue = Back.BLUE
b_yellow = Back.YELLOW
b_white = Back.WHITE
b_cyan = Back.CYAN
b_magenta = Back.MAGENTA

def logo():
    init()

    print ("")
    print ("     {} __ ___ __ {}_____ ___  __   ____  _____ ___   {} _ ___ ".format(blue,green,cyan))
    print ("     {}/ _] __/__\{}_   _| _ \/  \ / _/ |/ / __| _ \{}_{}_| | _,\ ".format(blue,green,white,cyan))
    print ("    {}| [/\ _| \/ |{}| | | v / /\ | \_|   <| _|| v /{}__{}| | v_/ ".format(blue,green,white,cyan))
    print ("     {}\__/___\__/ {}|_| |_|_\_||_|\__/_|\_\___|_|_\  {}|_|_|   {}v1.0 ".format(blue,green,cyan,white))
    print ("")
    print ("               {}<<< {}Tool coded by:{} @JRIC2002 {}>>>{}".format(red,yellow,white,red,white))
    print ("          {}<<< {}Description:{} Geolocalize IP Public {}>>>{}".format(red,yellow,white,red,white))
    print ("")

