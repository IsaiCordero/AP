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
    distance[first_node] = 0
    Q.enqueue(first_node)
    while not Q.isEmpty():
        v = Q.dequeue()
        for edges in graph.edges(v):
            arista = edges[1]
            if arista not in visitados:
                visitados.append(arista)
                Q.enqueue(arista)
                distance[arista] = distance[v] + 1
    return distance
