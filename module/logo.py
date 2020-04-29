#!/usr/bin/env python
# -*- coding: utf-8 -*-

#[*] Name of the Tool: GeoTrackerIP
#[*] Description: "Geolocalize IP Public"
#[*] Version: 2.0
#[*] Author: JRIC2002
#[*] Module of the Tool: GeoTrackerIP
#[*] Date of creation: 15/03/2019
#[*] Date of last update: 29/04/2020

""" Logo de la herramienta GeoTrackerIP. """

__author__ = "JRIC2002"
__copyright__ = "Copyright 2019, JRIC2002"
__credits__ = "JRIC2002"
__license__ = "GNU General Public License v3.0"
__version__ = "2.0"
__maintainer__ = "JRIC2002"
__email__ = "joselito18032002@gmail.com"
__status__ = "Production"

def logo():
    """ Imprime el logo de la herramienta GeoTrackerIP. """

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

    print("")
    print("     {} __ ___ __ {}_____ ___  __   ____  _____ ___   {} _ ___ ".format(blue, green, cyan))
    print("     {}/ _] __/__\{}_   _| _ \/  \ / _/ |/ / __| _ \{}__{}| | _,\ ".format(blue, green, white, cyan))
    print("    {}| [/\ _| \/ |{}| | | v / /\ | \_|   <| _|| v /{}__{}| | v_/ ".format(blue, green, white, cyan))
    print("     {}\__/___\__/ {}|_| |_|_\_||_|\__/_|\_\___|_|_\  {}|_|_|   {}v2.0 ".format(blue, green, cyan, white))
    print("")
    print("               {}<<< {}Tool coded by:{} @JRIC2002 {}>>>{}".format(red, yellow, white, red, white))
    print("          {}<<< {}Description:{} Geolocalize IP Public {}>>>{}".format(red, yellow, white, red, white))
    print("")

#START
if __name__ == "__main__":
    logo()
