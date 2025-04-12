#!/usr/bin/env/python
#-*- Coding: uft -*-
#Linea shebang: permite ejecutar este script directamente en sistemas unix/linux
#codificacion UFT-8 para permitir caracteres especioles

from flask import Flask, jsonify, request
#importamos flask para crear la app web, jsonify para devolver respuestas en JSON
#Y request para mejorar datos entramos (por ejemplo, de formularoos o JSON)

app = Flask(__name__)
#Creamos la instancia de la aplicacion flask

@app.route('/', methods=['GET'])
def hello():
    #definimos una ruta para el endpoint raiz "/" que responde a solicitudes get
    return 'Hello Wordl'
    # al acceder a la raiz del sitio devuelve este mensaje

if __name__ == "__main__":
    #este bloque se ejecuta solo si el script se ejecuta directamente (no importa como modulo)
    #app.run(host = '127.0.0.1', debug = True, port = 5000)
    #Linea comentada: ejecutaria el servidor localmente, solo accesible desde la misma maquina
    app.run(host = '0.0.0.0', debug = True, port = 5000)
    #Ejecuta la app en el host 0.0.0.0, lo cual la hace accesible desde otras maquinas de la red
    #el modo debug permite ver errores detallados y reinicia el servidor al derectar cambios
