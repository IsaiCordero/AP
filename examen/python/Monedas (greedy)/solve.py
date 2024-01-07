from sys import maxsize as infinite

def solve(coins, change):
    #Creo copia de la lista monedas y la ordeno
    lista = coins.copy()
    lista = sorted(lista, reverse = True)
    result = []
    #paso por los valores de esa lista ordenada
    for i in lista:
        #si una moneda es menor que el cambio actual
        if i <= change:
            #añadimos a la lista resultado la posicion de esa moneda en la lista original(sin ordenar)
            result.append(coins.index(i) + 1)
            #restamos al cambio el valor de la moneda
            change -= i
            #y ponemos en la lista original el valor a 0 de la posicion de esa moneda para no pillarla otra vez
            coins[coins.index(i)] = 0
    return result
