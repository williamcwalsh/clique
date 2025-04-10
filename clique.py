import itertools

def is_clique(graph, nodes):
    for u, v in itertools.combinations(nodes, 2):
        if v not in graph[u]:
            return False
    return True

def has_clique(graph, k):
    nodes = list(graph.keys())
    for subset in itertools.combinations(nodes, k):
        if is_clique(graph, subset):
            return True
    return False

# xample graphs
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'C'},
    'C': {'A', 'B'},
    'D': {'E'},
    'E': {'D'}
}

print(has_clique(graph, 3))  #True, since A-B-C form a 3-clique
