#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [*] Name of the Tool: GeoTrackerIP
# [*] Description: "Geolocalize IP Public"
# [*] Author: JRIC2002
# [*] Date: 15/03/2019

#MODULES

#External Modules

import requests
import json
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

#VERSION
def version():
    #Mensaje
    print("{}#GeoTrackerIP version 2.0".format(white))
    
#HELP MENU
def help_menu():
    #Logo
    geotrackerip_logo.logo()
    
    #Use
    print("{}Usage: python3 GeoTrackerIP.py [options]".format(white))
    print("")
    print("{}Options:".format(white))
    print("{}   -h, --help              Show this help message and exit.".format(white))
    print("{}   -v, --version           Show program's version number and exit.".format(white))
    print("")
    print("{}   Target:".format(white))
    print("{}      At least one of these options has to be provided to define the target(s).".format(white))
    print("")
    print("{}      -t, --target            IP Address or Domain to be analyzed.".format(white))

#ERROR OF ARGUMENT
def error_args():
    #Logo
    geotrackerip_logo.logo()

    #Use
    print("{}Usage: python3 GeoTrackerIP.py [options]".format(white))
    print("")
    print("{}GeoTrackerIP.py: Error: Invalid option.".format(white))
    print("{}Use -h or --help to see the options.".format(white))

#LOCATE IP
def geolocationIP(ip):
    #Logo
    geotrackerip_logo.logo()

    #Datos del usuario
    try:
        print("{}IP Address/Domain(URL):{} {}".format(blue, white, ip))
        while True:
            if "http://" in ip:
                ip = ip[7:]
            elif "www." in ip:
                ip = ip[4:]
            elif "https://" in ip:
                ip = ip[8:]
            else:
                break

        api_url = "http://ip-api.com/json/"
        res = requests.get(api_url+ip)
        datos = json.loads(res.content)

        #Resultados almacenados en variables
        target = ip
        direccion_ip = datos['query']
        asn = datos['as']
        ciudad = datos['city']
        pais = datos['country']
        codigo_pais = datos['countryCode']
        isp = datos['isp']
        latitud = datos['lat']
        longitud = datos['lon']
        organizacion = datos['org']
        codigo_region = datos['region']
        region = datos['regionName']
        timezone = datos['timezone']
        codigo_zip = datos['zip']
        google_maps = "https://www.google.com/maps/search/?api=1&query={},{}".format(latitud, longitud)

        #Imprimir los resultados
        print("")
        print("{}[{}*{}] {}Target:{} {}".format(green, white, green, white, green, target))
        print("{}[{}*{}] {}IP:{} {}".format(green, white, green, white, green, direccion_ip))
        print("{}[{}*{}] {}ASN:{} {}".format(green, white, green, white, green, asn))
        print("{}[{}*{}] {}City:{} {}".format(green, white, green, white, green, ciudad))
        print("{}[{}*{}] {}Country:{} {}".format(green, white, green, white, green, pais))
        print("{}[{}*{}] {}Country Code:{} {}".format(green, white, green, white, green, codigo_pais))
        print("{}[{}*{}] {}ISP:{} {}".format(green, white, green, white, green, isp))
        print("{}[{}*{}] {}Latitude:{} {}".format(green, white, green, white, green, latitud))
        print("{}[{}*{}] {}Longitude:{} {}".format(green, white, green, white, green, longitud))
        print("{}[{}*{}] {}Organization:{} {}".format(green, white, green, white, green, organizacion))
        print("{}[{}*{}] {}Region Code:{} {}".format(green, white, green, white, green, codigo_region))
        print("{}[{}*{}] {}Region Name:{} {}".format(green, white, green, white, green, region))
        print("{}[{}*{}] {}Timezone:{} {}".format(green, white, green, white, green, timezone))
        print("{}[{}*{}] {}Zip Code:{} {}".format(green, white, green, white, green, codigo_zip))
        print("{}[{}*{}] {}Google Maps:{} {}".format(green, white, green, white, green, google_maps))
        print("{}".format(white))
    except Exception:
        print("")
        print("{}Error: IP Address/Domain(URL) does not exist.{}".format(red, white))

#START
if len(sys.argv) == 3:
    if sys.argv[1] == "-t" or sys.argv[1] == "--target":
        geolocationIP(sys.argv[2])
    else:
        error_args()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        help_menu()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        version()
    else:
        error_args()
elif len(sys.argv) == 1:
    help_menu()
else:
    error_args()
