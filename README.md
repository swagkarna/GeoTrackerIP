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
**Menú de Ayuda**  
Para ver el menú de ayuda puedes utilizar la opción `-h` o `--help`.
```bash
python3 GeoTrackerIP.py --help
```

**Versión de la herramienta**  
Para ver la versión de la herramienta puedes utilizar la opción `-v` o `--version`.
```bash
python3 GeoTrackerIP.py --version
```

**Geolocalizar al objetivo**  
Puedes pasar como argumento la URL o la dirección IP del objetivo.
```bash
python3 GeoTrackerIP.py -t https://example.com
```

## Licencia
Vea el archivo de **Licencia** para más detalles.
