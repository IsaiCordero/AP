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

    # 1) Creamos el nodo raiz.
    # ...
    raiz = Node(0,[],0,capacity)
    # Lo añadimos a la lista de nodos vivos (alive)
    # ...
    alive.append(raiz)
    # Mientras haya nodos en la lista de nodos vivos
    # ...
    value = 0
    taken = []
    while len(alive) > 0:
        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.

        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)
        # Condiciones de poda
        # ...
        if current.room < 0:
            continue
        if current.estimate(items) < value:
            continue
        if current.index >= len(items):
            continue
        # Si no hemos llegado al final del árbol
        #    1) Ramificamos (branch) por la derecha (append)
        derecha = Node(current.index + 1, current.taken, current.value, current.room)
        alive.append(derecha)
        #    2) Ramificamos (branch) por la izquierda (append)
        # ...
        taken_izquierda = current.taken.copy()
        taken_izquierda.append(current.index+1)
        izquierda = Node(current.index + 1, taken_izquierda, current.value + items[current.index].value, current.room - items[current.index].weight)
        alive.append(izquierda)

        if current.room - items[current.index].weight > 0 and current.value + items[current.index].value > value:
            taken = taken_izquierda
            value = current.value + items[current.index].value

    return value, taken, visiting_order
