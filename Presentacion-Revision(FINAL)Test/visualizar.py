#!/usr/bin/env python3
"""Abre la presentación en un servidor HTTP local."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import webbrowser


def abrir_navegador(url):
    try:
        if webbrowser.open(url, new=2):
            return
    except webbrowser.Error:
        pass
    print(f"Abre {url} en Chrome o Edge.", flush=True)


def main():
    opciones = argparse.ArgumentParser(description=__doc__)
    opciones.add_argument("--puerto", type=int, default=4318, help="Puerto HTTP local (4318 por defecto).")
    opciones.add_argument("--sin-abrir", action="store_true", help="Muestra el enlace sin abrir el navegador.")
    argumentos = opciones.parse_args()

    carpeta = Path(__file__).resolve().parent
    if not carpeta.joinpath("index.html").is_file():
        opciones.error("Falta index.html en la carpeta de la presentación.")
    if not 0 <= argumentos.puerto <= 65535:
        opciones.error("El puerto debe estar entre 0 y 65535. Usa 0 para elegir uno disponible.")

    archivos = partial(SimpleHTTPRequestHandler, directory=str(carpeta))
    try:
        servidor = ThreadingHTTPServer(("127.0.0.1", argumentos.puerto), archivos)
    except OSError as error:
        opciones.error(f"No pude iniciar el servidor en el puerto {argumentos.puerto} ({error.strerror}). Usa --puerto para elegir otro.")

    with servidor:
        url = f"http://127.0.0.1:{servidor.server_port}/"
        print(f"Presentación disponible en {url}", flush=True)
        print("Deja esta ventana abierta durante la exposición. Pulsa Ctrl+C para cerrar.", flush=True)
        if not argumentos.sin_abrir:
            Thread(target=abrir_navegador, args=(url,), daemon=True).start()
        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor cerrado.")


if __name__ == "__main__":
    main()
