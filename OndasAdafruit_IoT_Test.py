# Test IoT con Adafruit IO
# Elaborado por: Arturo Daniel Péres Pérez  

from Adafruit_IO import Client
import time
import numpy as np

ADAFRUIT_IO_USERNAME = "Sustituir por IO_USERNAME"
ADAFRUIT_IO_KEY = "Sustituir por IO_KEY"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

def seno():
    T = 2 * np.pi  # Periodo completo de la onda
    num_puntos = 30  # Reducimos la cantidad de puntos para suavizar y optimizar envíos
    t = np.linspace(0, 1, num_puntos)  # Puntos uniformemente distribuidos
    x = 2 * t  # Escalamos el eje x
    y_sin = np.sin(T * x) / 10  # Generamos la onda con menor amplitud
    return y_sin.tolist()  # Devolvemos como lista para compatibilidad

def coseno():
    T = 2 * np.pi  # Periodo completo de la onda
    num_puntos = 30  # Misma cantidad de puntos que para el seno
    t = np.linspace(0, 1, num_puntos)  # Puntos uniformemente distribuidos
    x = 2 * t  # Escalamos el eje x
    y_cos = np.cos(T * x) / 10  # Generamos la onda con menor amplitud
    return y_cos.tolist()  # Devolvemos como lista para compatibilidad

def sendSen(y_sin):   
    for i in range(len(y_sin)):
        aio.send("sen", y_sin[i])
        time.sleep(2)  # Incrementamos el tiempo entre envíos para reducir saturación
    print("Datos de seno enviados exitosamente...")

def sendCos(y_cos):   
    for i in range(len(y_cos)):
        aio.send("cos", y_cos[i])
        time.sleep(2)  # Incrementamos el tiempo entre envíos para reducir saturación
    print("Datos de coseno enviados exitosamente...")

# Envío de datos a Adafruit
FnSen = seno()
sendSen(FnSen)

FnCos = coseno()
sendCos(FnCos)