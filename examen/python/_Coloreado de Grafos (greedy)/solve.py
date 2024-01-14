
def greedy_coloring(graph, order_nodes):
    node_colors =[0] * len(order_nodes)
    #recorre los nodos en el orden dado
    for i, node in enumerate(order_nodes):
        #se obtienen los colores de los vecinos
        vecinos = [node_colors[order_nodes.index(vecino)] for vecino in graph.neighbors(node) if order_nodes.index(vecino) < i]

        color = 0
        #se usa el color mas bajo no usado
        while color in vecinos:
            color += 1
        #se asignan colores
        node_colors[i] = color
    return node_colors
    