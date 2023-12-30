import networkx as nx

def build_digraph_with_weights():
    """ 
    Read data from the standard input and build the corresponding
    directed graph with weights. Nodes numbering starts with number
    1 (that is, nodes are 1,2,3,...)
    """

    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])

    # Paso 1: Crear grafo direcional con num_nodes
    graph = nx.DiGraph()
    for nodes in range(1,num_nodes+1):
        graph.add_node(nodes)

    # Paso 2: Añadir los vértices del grafo
    for edges in range(1,num_edges+1):
        arista = input().split()
        graph.add_edges_from([(int(arista[0]), int(arista[1]), {'weight': arista[2]})])

    return graph
