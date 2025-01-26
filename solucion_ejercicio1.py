import tdarecuperatorio as tda
from random import choice


consultorios = [1,2,3,4,5,6,7]

turnos = tda.Cola()
# creamos la fila de los 20 turnos
for i in range(20): turnos.encolar(i)

# print(turnos.lista_cola)
for t in reversed(turnos.lista_cola):
    print(f"turno nro{turnos.desencolar()} - consultorio nro{choice(consultorios)}")