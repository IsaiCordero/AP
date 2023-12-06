import networkx as nx


def build_digraph_with_weights():
    """
    Read data from the standard input and build the corresponding
    directed graph with weights. Nodes numbering starts with number
    1 (that is, nodes are 1,2,3,...)
    """

    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    # Paso 1: Crear grafo direcional con num_nodes
    graph = nx.DiGraph()
    for i in range(1, num_nodes + 1):
        graph.add_node(i)

    for i in range(1, num_edges + 1):
        aristas = input().split()
        graph.add_edges_from([(int(aristas[0]), int(aristas[1]), {'weight': aristas[2]})])

    # Paso 2: Añadir los vértices del grafo

    return graph
