import networkx as nx
from solve import *

# Crear un grafo bipartito
B = nx.Graph()
left_nodes = ['v1','v3', 'v5','v7','v9']
right_nodes = ['v2','v4', 'v6','v8','v10']
B.add_nodes_from(left_nodes, bipartite=0)
B.add_nodes_from(right_nodes, bipartite=1)

# Agregar aristas según la condición dada
for i in range(len(left_nodes)):
    for j in range(len(right_nodes)):
        if i!=j:
            B.add_edge(left_nodes[i], right_nodes[j])

nodes = B.nodes()

#cambiamos el orden
order_list = input().split()
order_dict = {v: i for i, v in enumerate(order_list)}  # Creamos un diccionario que mapea cada valor a su índice

nodes = sorted(nodes, key=lambda x: order_dict[x[1:]])

color_map = greedy_coloring(B, order_nodes=nodes)

print(color_map)
