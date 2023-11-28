import networkx   as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}                 # Diccionario con la distancia desde 
                                  # firstNode al resto de los nodos.
    for node in graph.nodes():
        distance[node] = infinite

    # solve it here!
    # ...
    Q = Queue()
    visitados = []
    visitados.append(first_node)
    Q.enqueue(first_node)
    distance[first_node] = 0
    while not Q.isEmpty():
        nodo = Q.dequeue()
        edges = graph.edges(nodo)
        for nodos in edges:
            edge = nodos[1]
            if edge not in visitados:
                visitados.append(edge)
                Q.enqueue(edge)
                distance[edge] = distance[nodo] + 1

    return distance
