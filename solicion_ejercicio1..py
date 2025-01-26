# Ejercicio 1

# Un centro de Salud abre a las 8 AM y otorga 20 turnos desde el número 0 al 19 todos los
# días. 

# El centro de salud posee 7 consultorios del 1 al 7 para atender a los pacientes.

# Ud. debe realizar un programa que otorgue los números a cada paciente, estos esperan ser
# llamados, por los consultorios = [1,2,3,4,5,6,7].

# Los consultorios son asignados aleatoriamente hasta terminar de atender a todos los clientes.

# ALGORÍMOS Y PROGRAMACIÓN 3
# Se le otorgarán los TDA correspondientes de Pila y Cola, estarán en un archivo llamado
# tda_parcial.py este debe alojarse en la misma carpeta donde está ejecutando su programa.
# Recuerde la forma de importar clases desde otro archivo, abra su archivo y en la primer

import tdarecuperatorio as tda
from random import choice


consultorios = [1,2,3,4,5,6,7]

turnos = tda.Cola()
# creamos la fila de los 20 turnos
for i in range(20): turnos.encolar(i)

# print(turnos.lista_cola)
for t in reversed(turnos.lista_cola):
    print(f"turno nro{turnos.desencolar()} - consultorio nro{choice(consultorios)}")