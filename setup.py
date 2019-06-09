#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [*] Name of the Tool: GeoTrackerIP
# [*] Description: "Geolocalize IP Public"
# [*] Author: JRIC2002
# [*] Date: 15/03/2019

#MODULOS

import itertools
import time
import os
import sys

#COLORES EN CODIGO ANSI

#Foreground

a_black = "\033[1;30m"
a_red = "\033[1;31m"
a_green = "\033[1;32m"
a_yellow = "\033[1;33m" 
a_blue = "\033[1;34m"
a_magenta = "\033[1;35m"
a_cyan = "\033[1;36m"
a_white = "\033[1;37m"

#Background

ab_black = "\033[1;40m"
ab_red = "\033[1;41m"
ab_green = "\033[1;42m"
ab_yellow = "\033[1;43m"
ab_blue = "\033[1;44m"
ab_magenta = "\033[1;45m"
ab_cyan = "\033[1;46m"
ab_white = "\033[1;47m"

#LIMPIAR CONSOLA

def limpiar():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
        
#BANNER

def banner():

    print ("")
    print ("     {} __ ___ __ {}_____ ___  __   ____  _____ ___   {} _ ___ ".format(a_blue, a_green, a_cyan))
    print ("     {}/ _] __/__\{}_   _| _ \/  \ / _/ |/ / __| _ \{}_{}_| | _,\ ".format(a_blue, a_green, a_white, a_cyan))
    print ("    {}| [/\ _| \/ |{}| | | v / /\ | \_|   <| _|| v /{}__{}| | v_/ ".format(a_blue, a_green, a_white, a_cyan))
    print ("     {}\__/___\__/ {}|_| |_|_\_||_|\__/_|\_\___|_|_\  {}|_|_|   {}v1.0 ".format(a_blue, a_green, a_cyan, a_white))
    print ("")
    print ("               {}<<< {}Tool coded by:{} @JRIC2002 {}>>>{}".format(a_red, a_yellow, a_white, a_red, a_white))
    print ("          {}<<< {}Description:{} Geolocalize IP Public {}>>>{}".format(a_red, a_yellow, a_white, a_red, a_white))
    print ("")

#INSTALACION...

def instalacion():
    
    print("")
    bucle = itertools.cycle("/-|-\|")
    for i in range(30):
        print("{}[{}*{}] {}Instalando modulos...{}{}".format(a_cyan, a_white, a_cyan, a_green, next(bucle), a_white), end='\r')
        time.sleep(0.1)
    
    print ("")
    print ("")
    os.system("pip3 install colorama")
    os.system("pip3 install requests")
    print ("")
    print ("                        {}>> Instalacion Completa <<{}".format(a_blue, a_white))
    print ("")
    time.sleep(1)

#ELEGIR OPCION

def pregunta():

        limpiar()
        banner()
        print ("{}[{}#{}] {}Desea ejecutar la herramienta GeoTrackerIP:".format(a_cyan, a_white, a_cyan, a_magenta))
        print ("")
        print ("    {}[{}01{}] {}Si".format(a_green, a_white, a_green, a_yellow))
        print ("")
        print ("    {}[{}02{}] {}No".format(a_green, a_white, a_green, a_yellow))
        print ("")

        opcion = input("{}[{}*{}] Choose an Option {}>> ".format(a_green, a_white, a_green, a_white))

        if opcion == "1" or opcion == "01":
            limpiar()
            os.system("python3 GeoTrackerIP.py")
        elif opcion == "2" or opcion == "02":
            time.sleep(1)
            sys.exit()
        else:
            time.sleep(1)
            pregunta()

instalacion()
pregunta()

