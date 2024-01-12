import networkx as nx

def create_wheel_graph():
    """Crea un wheel graph, centrado en 'g'

    Returns:
        tuple: Un grafo de NetworkX y la lista de nodos.
    """
    G = nx.Graph()
    nodos = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    G.add_nodes_from(nodos)
    aristas = [('a', 'g'), ('b', 'g'), ('c', 'g'), ('d', 'g'), ('e', 'g'), ('f', 'g'),
               ('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'a')]
    G.add_edges_from(aristas)
    return G, nodos