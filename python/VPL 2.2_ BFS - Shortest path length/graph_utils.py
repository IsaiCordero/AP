import networkx as nx


def build_graph():
    """
    Read data from the standard input and build the corresponding
    nondirected graph without weights. Nodes numbering starts with
    number 1 (that is, nodes are 1,2,3,...)
    """
    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    # Paso 1: Crear el grafo no-dirigido con sus vértices
    graph = nx.Graph()
    for nodes in range(1,num_nodes+1):
        graph.add_node(nodes)
    # Paso 2: Añadirle las aristas
    for edges in range(1,num_edges+1):
        aristas = input().split()
        graph.add_edge(int(aristas[0]), int(aristas[1]))
    return graph
