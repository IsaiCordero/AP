from node import *


def solve_branch_and_bound_DFS(capacity, items, record_visiting_order=False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: Por ahora sólo devuelve la lista de nodos visitados
    """

    # Completa este código para realizar el recorrido DFS; tienes
    # indicados los sitios que debes completar con tres puntos
    # suspensivos ("...")

    # Utilizamos la lista 'alive' como nuestra pila de nodos vivos
    # (pendientes de visitar) para programar nuestro recorrido DFS.

    alive = []

    # Utilizamos la lista Visiting_Order como el registro de nodos
    # visitados (el contenido final de esta lista lo utiliza el VPL
    # para comprobar que nuestro recorrido DFS es correcto).

    visiting_order = []

    # 1) Creamos el nodo raiz (en este VPL todavía no utilizamos los
    #    parámetros taken, value, room, con lo que se inicializan con
    #    lista vacía y 0). El único valor necesario en el nodo es el
    #    indice al primer elemento de la lista (index = 0).
    # ...
    root = Node(0, [], 0, capacity)

    # Lo añadimos a la lista de nodos vivos (alive)
    # ...
    alive.append(root)
    # Mientras haya nodos en la lista de nodos vivos
    # ...
    valor = 0
    taken = []
    while len(alive) > 0:  # sustituir el True por la condición que considere más adecuada

        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.

        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)

        # si el indice actual es mayor a los que hay en la lista sigue con el siguiente nodo
        if current.index >= len(items):
            continue

        #si el tamaño disponible es menor a cero pasa al siguiente nodo
        if current.room < 0:
            continue

        #si el valor es mayor a la capacidad de la mochila pasa al siguiente nodo
        if valor > current.estimate(items):
            continue
        # Si no hemos llegado al final del árbol

        #    1) Ramificamos (branch) por la derecha (append)
        taken_derecha = current.taken.copy()
        derecha = Node(current.index + 1, taken_derecha, current.value, current.room)
        alive.append(derecha)
        #    2) Ramificamos (branch) por la izquierda (append)
        # ...
        taken_izquierda = current.taken.copy()
        taken_izquierda.append(current.index + 1)
        izquierda = Node(current.index + 1, taken_izquierda, items[current.index].value + current.value,current.room - items[current.index].weight)
        alive.append(izquierda)


        #si tenemos espacio en la mochila y el valor actual es mejor que el anterior los actualizamos
        if current.room - items[current.index].weight > 0 and current.value + items[current.index].value > valor:
            valor = current.value + items[current.index].value
            taken = taken_izquierda

    return valor, taken, visiting_order
