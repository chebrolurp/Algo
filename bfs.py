# defaultdict does not give key error very useful to represent a graph
from collections import defaultdict

# input: edges and  output: dictionary(adjacency list)
def Graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def bfs(visited,graph, node):
    
    queue = []
    
    # starting node
    queue.append(node)
    visited.add(node)
    
    while queue:

        s = queue.pop(0)
        print (s, end = " ") 

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
nodes = ['a','b','c','d','e','f','g','h','i','j']
edges = [('a','b'),('b','c'),('c','a'),('c','d'),('d','f'),('e','f'),('f','i'),('i','a'),('d','b'),
         ('c','j'),('c','e'),('g','h'),('h','e'),('g','j'),('f','g')]

graph = Graph(edges)

visited = set()
print('BFS')
bfs(visited,graph, 'i')
print()
