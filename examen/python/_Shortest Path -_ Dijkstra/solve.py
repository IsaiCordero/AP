import networkx as nx
from sys import maxsize as infinite
from simple_queue import *


def solve(graph, from_node, to_node):
    #calculo de las distancias
    def distancias(graph, start_node):
        distances = {node: infinite for node in graph.nodes}
        distances[start_node] = 0
        return distances
    #calculo de dijkstra
    def dijkstra(graph, start_node, end_node):
        #calcula la distancia actual, crea la cola y añade el primer nodo a la cola
        distances = distancias(graph,start_node)
        Q = Queue()
        Q.enqueue(start_node)
        #mientras la cola no esté vacia saca un nodo
        while not Q.isEmpty():
            v = Q.dequeue()
            #para los vecinos calcula los pesos
            for neighbors in graph.neighbors(v):
                peso = graph[v][neighbors]['weight']
                #si la distancia actual mas el peso es menor que la del vecino se le da esa distancia y se añade a la cola
                if distances[v] + peso < distances[neighbors]:
                    distances[neighbors] = distances[v] + peso
                    Q.enqueue(neighbors)
        return distances[end_node]

    distancia_minima = dijkstra(graph,from_node,to_node)
    return distancia_minima