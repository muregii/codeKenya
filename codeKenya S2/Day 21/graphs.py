#from collections import defaultdict
#
#def build_graph_adj(edges):
#    graph = defaultdict(list)
#    for x, y in edges:
#        graph[x].append(y)
#        graph[y].append(x)
#        # uncomment the above line if the graph is undirected
#    
#    return graph
#
#edges = [[0, 1], [1, 2], [2, 0], [2, 3]]
#
#
#
#def build_graph(edges, directed=False):
#    """
#    Build a graph using an adjacency list representation.
#
#    :param edges: List of [u, v] edges
#    :param directed: If True, graph is directed; if False, graph is undirected
#    :return: adjacency list as a dict
#    """
#    adjacency_list = defaultdict(list)
#
#    for u, v in edges:
#        adjacency_list[u].append(v)
#        if not directed:
#            adjacency_list[v].append(u)  # For undirected graphs
#
#    return adjacency_list
#
## Example edges
#edges = [[0, 1], [1, 2], [2, 0], [2, 3]]
#
## Build undirected graph
#graph = build_graph(edges, directed=False)
#
## Print adjacency list nicely
#for node, neighbors in graph.items():
#    print(f"{node}: {neighbors}")
#
#res = build_graph(edges)
#print(res)

class GraphNode:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

graph = [["Raydon","Muregi","Mbehero"],
         ["Chilson","Litsalia","Mbehero"],
         ["Ian","Slade","Ashivende"]]

raydon = graph[0][2]
chilson = graph[1][2]
ian = graph[2][2]

print(raydon)
print(chilson)
print(ian)

zero = GraphNode(0, [1, 2, 3])
one = GraphNode(1, [0, 2, 3])

#print(f"{zero.val} -> {zero.neighbors}")

#print(f"{one.val} -> {one.neighbors}")