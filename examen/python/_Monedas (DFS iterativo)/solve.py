from sys import maxsize as infinite
from simple_stack import *
def solve(coins, change):
    pila = Stack()
    visitados = []
    #se crea el estado incial y se añade a la pila
    estadoInicial = (0,0,[])
    pila.push(estadoInicial)
    #mientras esta pila no esté vacia se hace un pop de ella
    while not pila.isEmpty():
        current_index, current_sum, selected_index = pila.pop()
        #si la suma actual de dinero es igual al cambio entonces se devuelve una lista de las posiciones de esas monedas
        if current_sum == change:
            return [indices + 1 for indices in selected_index]
        #si no se ha llegado al final de la lista se crean las variables de la suma actual + la moneda de la lista y el del indice actual
        if current_index < len(coins):
            suma = current_sum + coins[current_index]
            indices = selected_index + [current_index]
            #si no se han visitado los nuevos y la suma es menor o igual que el cambio actual, se añaden a la pila y a los visitados
            if (current_index + 1, suma) not in visitados and suma <= change:
                pila.push((current_index + 1, suma, indices))
                visitados.append((current_index + 1, suma))
            #si no se han visitados los primeros se añaden a pila y a la lista visitados
            if (current_index + 1, current_sum) not in visitados:
                pila.push((current_index + 1, current_sum, selected_index))
                visitados.append((current_index + 1, current_sum))
    return None
