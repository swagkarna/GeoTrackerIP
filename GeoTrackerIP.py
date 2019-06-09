#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [*] Name of the Tool: GeoTrackerIP
# [*] Description: "Geolocalize IP Public"
# [*] Author: JRIC2002
# [*] Date: 15/03/2019

#IMPORTACION DE MODULOS

import requests
import json
from colorama import init, Fore, Back, Style

from modules.banner import geotracker_ip_logo

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

def geolocationIP():
    init()
    
    #Banner

    geotracker_ip_logo.logo()

    #Datos del usuario

    ip = input("{}Enter IP Address:{} ".format(blue, white))
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
    
    print ("")
    print ("{}[{}*{}] {}Target:{} {}".format(green, white, green, white, green, target))
    print ("{}[{}*{}] {}IP:{} {}".format(green, white, green, white, green, direccion_ip))
    print ("{}[{}*{}] {}ASN:{} {}".format(green, white, green, white, green, asn))
    print ("{}[{}*{}] {}City:{} {}".format(green, white, green, white, green, ciudad))
    print ("{}[{}*{}] {}Country:{} {}".format(green, white, green, white, green, pais))
    print ("{}[{}*{}] {}Country Code:{} {}".format(green, white, green, white, green, codigo_pais))
    print ("{}[{}*{}] {}ISP:{} {}".format(green, white, green, white, green, isp))
    print ("{}[{}*{}] {}Latitude:{} {}".format(green, white, green, white, green, latitud))
    print ("{}[{}*{}] {}Longitude:{} {}".format(green, white, green, white, green, longitud))
    print ("{}[{}*{}] {}Organization:{} {}".format(green, white, green, white, green, organizacion))
    print ("{}[{}*{}] {}Region Code:{} {}".format(green, white, green, white, green, codigo_region))
    print ("{}[{}*{}] {}Region Name:{} {}".format(green, white, green, white, green, region))
    print ("{}[{}*{}] {}Timezone:{} {}".format(green, white, green, white, green, timezone))
    print ("{}[{}*{}] {}Zip Code:{} {}".format(green, white, green, white, green, codigo_zip))
    print ("{}[{}*{}] {}Google Maps:{} {}".format(green, white, green, white, green, google_maps))
    print ("{}".format(white))

geolocationIP()
