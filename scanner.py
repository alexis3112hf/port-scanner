import socket
import threading
import json
import time
from queue import Queue

# Cargar nombres de servicios comunes
with open("services.json", "r") as f:
    SERVICES = json.load(f)

open_ports = []
queue = Queue()

def scan_port(host, port):
    start_time = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((host, port))
        latency = round((time.time() - start_time) * 1000, 2)

        if result == 0:
            service = SERVICES.get(str(port), "Desconocido")
            open_ports.append((port, service, latency))

    except:
        pass
    finally:
        sock.close()

def worker(host):
    while not queue.empty():
        port = queue.get()
        scan_port(host, port)
        queue.task_done()

def generate_report(host):
    html = """
    <html>
    <head>
    <title>Reporte Port Scanner</title>
    </head>
    <body>
    <h1>Reporte de puertos abiertos</h1>
    <p>Host escaneado: <b>{}</b></p>
    <table border="1" cellpadding="5">
    <tr><th>Puerto</th><th>Servicio</th><th>Latencia (ms)</th></tr>
    """.format(host)

    for port, service, latency in open_ports:
        html += f"<tr><td>{port}</td><td>{service}</td><td>{latency}</td></tr>"

    html += "</table></body></html>"

    with open("report.html", "w") as f:
        f.write(html)

    print("\n📄 Reporte generado: report.html")

def main():
    host = input("Ingrese la IP o dominio a escanear: ")

    print("\nEscaneando...")

    for port in range(1, 1025):
        queue.put(port)

    threads = []

    for _ in range(100):  # 100 hilos
        t = threading.Thread(target=worker, args=(host,))
        t.daemon = True
        t.start()
        threads.append(t)

    queue.join()

    print("\nPuertos abiertos encontrados:")
    for port, service, latency in open_ports:
        print(f"[{port}] {service} - {latency} ms")

    generate_report(host)

if __name__ == "__main__":
    main()

