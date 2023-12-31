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
    raiz = Node(0,[],0, capacity)
    # Lo añadimos a la lista de nodos vivos (alive)
    # ...
    alive.append(raiz)
    # Mientras haya nodos en la lista de nodos vivos
    # ...
    best_solution = 0
    taken = []
    while len(alive) > 0:
        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.

        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)
        # Condiciones de poda
        # ...
        if current.room < 0:  #se comprueba el espacio de la mochila
            continue
        if current.estimate(items) < best_solution:   # se comprueba si mejora la solucion actual
            continue
        if current.index >= len(items):      # se comprueba que no estemos al final de arbol
            continue
        # Si no hemos llegado al final del árbol
        #    1) Ramificamos (branch) por la derecha (append)
        #    2) Ramificamos (branch) por la izquierda (append)
        # ...
        derecha = Node(current.index + 1, current.taken, current.value, current.room)  #solo aumenta el index
        alive.append(derecha)
        taken_izquierda = current.taken.copy()
        taken_izquierda.append(current.index + 1)
        izquierda = Node(current.index + 1, taken_izquierda, current.value + items[current.index].value, current.room - items[current.index].weight) #aumenta index, taken y value pero disminuye el room(capacidad de la mochila)
        alive.append(izquierda)

        if current.room - items[current.index].weight > 0 and current.value + items[current.index].value > best_solution:  # si el valor es mejor al que teniamos y hay capaicdad en la mochila, lo actualizamos
            best_solution = current.value + items[current.index].value
            taken = taken_izquierda
    return best_solution, taken, visiting_order