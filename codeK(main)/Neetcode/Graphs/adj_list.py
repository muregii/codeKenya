class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbours = []


#adj_list = {"A": [], "B": []}

edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adj_list = {}

for src, dst in edges:
    if src not in adj_list:
        adj_list[src] = []
    if dst not in adj_list:
        adj_list[dst] = []
    adj_list[src].append(dst) # A -> B -> C 

print(adj_list.keys())
print(adj_list.values())