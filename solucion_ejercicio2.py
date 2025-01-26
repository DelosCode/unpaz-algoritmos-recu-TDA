from tdarecuperatorio import ListaOrdenada

TARGET = 5

lista_ordenada = ListaOrdenada()
for n in range(1,11): lista_ordenada.agregar(n)

lista_ordenada.ver()
print(f"el numero {TARGET} se encuentra en la lista?: {lista_ordenada.buscar(TARGET)}")
lista_ordenada.remover(TARGET)
print(f"el numero {TARGET} se encuentra en la lista?: {lista_ordenada.buscar(TARGET)}")
lista_ordenada.ver()