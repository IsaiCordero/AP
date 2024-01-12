import networkx as nx


def dsat_coloring(graph, order_nodes):
    # Implementación del algoritmo DSatur
    nodes_colors = {}
    for node in order_nodes:
        nodes_colors[node] = None

    # Escribir el código a partir de aquí
    # _____________________________________________________________________
    #ordenamos el grafo para poder seleccionar bien los nodos
    grafoOrdenado = sorted(graph.nodes(), key = lambda x: graph.degree[x], reverse=True)
    saturacion = {node : 0 for node in order_nodes}
    for node in grafoOrdenado:
        vecinos = set(graph.neighbors(node))
        colores = {nodes_colors[vecino] for vecino in vecinos if nodes_colors[vecino] is not None}
        vecinosColoreados = len(colores)
        saturacion[node] = vecinosColoreados
    for node in grafoOrdenado:
        if nodes_colors[node] is None:
            vecinos = set(graph.neighbors(node))
            colores = {nodes_colors[vecino] for vecino in vecinos if nodes_colors[vecino] is not None}
            color = 0
            while color in colores:
                color += 1
            nodes_colors[node] = color
    # _____________________________________________________________________
    return [nodes_colors[node] for node in order_nodes]

