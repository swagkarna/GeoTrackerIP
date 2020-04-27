# GeoTrackerIP
![GeoTracker - Version](https://img.shields.io/badge/GeoTrackerIP-v2.0-brightgreen)
![Release - Stable](https://img.shields.io/badge/Release-Stable-brightgreen)
![Supported OS - Linux](https://img.shields.io/badge/Supported%20OS-Linux-blue)

GeoTrackerIP es una herramienta que te permite obtener: Ubicación Geográfica de una Dirección IP, ISP(Proveedor de Servicios de Internet), Ciudad-País de la IP, entre otros.

![GeoTrackerIP - Screenshot](https://github.com/JRIC2002/GeoTrackerIP/blob/master/.Screenshots/GeoTrackerIP-Screenshot[01].jpg)

## Información
Esta herramienta es solo para fines educativos. No me hago responsable por el mal uso o daño causado por este programa.

## Características
* Automatiza el proceso de Geolocalización.
* Identifica la dirección IP del servidor.
* Muestra detalles de la dirección IP.

## Instalación
1. Clonar el repositorio **GeoTrackerIP**.

```bash
git clone https://github.com/JRIC2002/GeoTrackerIP
```

2. Entrar a la carpeta **GeoTrackerIP**.

```bash
cd GeoTrackerIP
```

3. Dar permisos de ejecución a los archivos.

```bash
chmod +x GeoTrackerIP.py
chmod +x install.py
```
4. Ejecutar el archivo de instalación **install.py**.

```bash
python3 install.py
```

5. Ya puedes ejecutar la herramienta **GeoTrackerIP**.

```bash
python3 GeoTrackerIP.py
```

## Uso

```bash
u0_a107@localhost ~/GeoTrackerIP> python3 GeoTrackerIP.py

      __ ___ __ _____ ___  __   ____  _____ ___    _ ___
     / _] __/__\_   _| _ \/  \ / _/ |/ / __| _ \__| | _,\
    | [/\ _| \/ || | | v / /\ | \_|   <| _|| v /__| | v_/
     \__/___\__/ |_| |_|_\_||_|\__/_|\_\___|_|_\  |_|_|   v2.0

               <<< Tool coded by: @JRIC2002 >>>
          <<< Description: Geolocalize IP Public >>>

Usage: python3 GeoTrackerIP.py [options]

Options:
   -h, --help              Show this help message and exit.
   -v, --version           Show program's version number and exit.

   Target:
      At least one of these options has to be provided to define the target(s).

      -t, --target            IP Address or Domain to be analyzed.
```

## Licencia
Vea el archivo de **Licencia** para más detalles.
