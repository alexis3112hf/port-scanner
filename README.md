# 🛡️ Port Scanner Pro
Escáner de puertos avanzado escrito en Python. Permite analizar puertos abiertos en un host, identificar servicios comunes y medir la latencia de respuesta. Ideal para prácticas de ciberseguridad y análisis básico de red.

---

## 🚀 Características
- 🔍 Escaneo de puertos del 1 al 1024  
- ⚡ Escaneo rápido usando *multithreading*  
- 📡 Identificación automática de servicios (HTTP, SSH, FTP, etc.)  
- ⏱️ Medición de latencia por puerto  
- 📄 Generación automática de reporte en **HTML**  
- 🛑 Detección silenciosa usando sockets (TCP Connect Scan)  

---

## 🧠 ¿Cómo funciona?
1. El usuario ingresa una IP o dominio.  
2. El script lanza 100 hilos para escanear puertos rápidamente.  
3. Se prueba conexión vía TCP a cada puerto.  
4. Si el puerto está abierto:
   - Se identifica el servicio (si está en `services.json`)  
   - Se calcula la latencia  
5. Al finalizar, se genera un archivo `report.html` con todos los resultados.

---

## ▶️ Ejecución

### 1. Instala Python (si no lo tienes)
sudo pacman -S python

### 2. Ejecutar el scanner
python scanner.py

## Ejemplo

Ingrese la IP o dominio a escanear: 192.168.1.1

Puertos abiertos encontrados:
[22] SSH - 1.82 ms
[80] HTTP - 3.51 ms

---

## En el Archivo services.json puedes agregar más puertos

{
  "22": "SSH",
  "80": "HTTP",
  "443": "HTTPS",
  "3306": "MySQL",
  "3389": "RDP",
  "8080": "HTTP Proxy"
}

---

## Reporte de HTML 
report.html
Contiene una tabla con:
  - Puerto
  - Servicio
  - Latencia
  - Host escaneado
