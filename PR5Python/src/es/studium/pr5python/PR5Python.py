# coding: utf-8

'''
Created on 27 ene. 2020

@author: JQ
'''


import random
import statistics as stats
from nt import stat
from pstats import Stats

'''
print("¿Cómo se llamará tu lista?")
nombreFichero = input()



print("Introduzca la primera característica: ")
primeraCaracteristica = input()

print("---- INDIQUE LOS RANGOS ----")
print("¿Cúal será el rango mínimo?")
rangoMinimo1 = input()
print("¿Cúal será el rango máximo?")
rangoMaximo1 = input()



print("Introduzca la segunda característica: ")
segundaCaracteristica = input()

print("---- INDIQUE LOS RANGOS ----")
print("¿Cúal será el rango mínimo?")
rangoMinimo2 = input()
print("¿Cúal será el rango máximo?")
rangoMaximo2 = input()



print("Introduzca la tercera característica: ")
segundaCaracteristica = input()

print("---- INDIQUE LOS RANGOS ----")

print("¿Cúal será el rango mínimo?")
rangoMinimo3 = input()
print("¿Cúal será el rango máximo?")
rangoMaximo3 = input()


print("Introduzca la cuarta característica: ")
segundaCaracteristica = input()

print("---- INDIQUE LOS RANGOS ----")

print("¿Cúal será el rango mínimo?")
rangoMinimo4 = input()
print("¿Cúal será el rango máximo?")
rangoMaximo4 = input()


print("Introduzca la quinta característica: ")
segundaCaracteristica = input()

print("---- INDIQUE LOS RANGOS ----")

print("¿Cúal será el rango mínimo?")
rangoMinimo5 = input()
print("¿Cúal será el rango máximo?")
rangoMaximo5 = input()


try:
    f = open(nombreFichero + ".txt", "a")
except Exception:
    exit()




for i in range(10):
    
    f.write((str(random.randint(int(rangoMinimo1), int(rangoMaximo1)))) + (str(random.randint(int(rangoMinimo2), int(rangoMaximo2)))) + (str(random.randint(int(rangoMinimo3), int(rangoMaximo3)))) + (str(random.randint(int(rangoMinimo4), int(rangoMaximo4)))) + (str(random.randint(int(rangoMinimo5), int(rangoMaximo5)))) + "\n")

f.close()
'''

    


print("¿Cúal es el nombre del archivo que quieres abrir?")
respuesta = input()


try:
    f = open(respuesta + ".txt", "r")
except Exception:
    exit()



puntosPorPartido = []
faltasPorPartido = []
rebotesPorPartido = []
tirosLibresPorPartido = []
triplesPorPartido = []


for line in f:
    
    puntosPorPartido.append(int(line[0]))
    faltasPorPartido.append(int(line[1]))
    rebotesPorPartido.append(int(line[2]))
    tirosLibresPorPartido.append(int(line[3]))
    triplesPorPartido.append(int(line[4]))
    



print("---- PUNTOS POR PARTIDO ----")
print("Media: " + str(stats.mean(puntosPorPartido)) + " || " + "Moda: " + str(stats.mode(puntosPorPartido)) + " || " + "Máximo: " + str(max(puntosPorPartido)) + " || " + "Mínimo: " + str(min(puntosPorPartido)) + " || " + "Varianza: " + str(stats.variance(puntosPorPartido)))



print("---- FALTAS POR PARTIDO ----")
print("Media: " + str(stats.mean(faltasPorPartido)) + " || " + "Moda: " + str(stats.mode(faltasPorPartido)) + " || " + "Máximo: " + str(max(faltasPorPartido)) + " || " + "Mínimo: " + str(min(faltasPorPartido)) + " || " + "Varianza: " + str(stats.variance(faltasPorPartido)))

print("---- REBOTES POR PARTIDO ----")
print("Media: " + str(stats.mean(rebotesPorPartido)) + " || " + "Moda: " + str(stats.mode(rebotesPorPartido)) + " || " + "Máximo: " + str(max(rebotesPorPartido)) + " || " + "Mínimo: " + str(min(rebotesPorPartido)) + " || " + "Varianza: " + str(stats.variance(rebotesPorPartido))) 

print("---- TIROS LIBRES POR PARTIDO ----")
print("Media: " + str(stats.mean(tirosLibresPorPartido)) + " || " + "Moda: " + str(stats.mode(tirosLibresPorPartido)) + " || " + "Máximo: " + str(max(tirosLibresPorPartido)) + " || " + "Mínimo: " + str(min(tirosLibresPorPartido)) + " || " + "Varianza: " + str(stats.variance(tirosLibresPorPartido))) 

print("---- TRIPLES POR PARTIDO ----")
print("Media: " + str(stats.mean(triplesPorPartido)) + " || " + "Moda: " + str(stats.mode(triplesPorPartido)) + " || " + "Máximo: " + str(max(triplesPorPartido)) + " || " + "Mínimo: " + str(min(triplesPorPartido)) + " || " + "Varianza: " + str(stats.variance(triplesPorPartido))) 


'''
---TABLA--
names = ["Puntos por Partida", "Faltas por partido", "Rebotes por Partido"]
values = [puntosPorPartido, faltasPorPartido, rebotesPorPartido]
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
'''




