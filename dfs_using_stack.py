# defaultdict does not give key error very useful to represent a graph
from collections import defaultdict

# input: edges and  output: dictionary(adjacency list)
def Graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def dfs(visited,graph, node):
    
    stack = []
    
    # starting node
    stack.append(node)
    visited.append(node)
    
    while stack:

        s = stack.pop(-1)
        print (s, end = " ") 

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

            
nodes = ['a','b','c','d','e','f','g','h','i','j']
edges = [('a','b'),('b','c'),('c','a'),('c','d'),('d','f'),('e','f'),('f','i'),('i','a'),('d','b'),
         ('c','j'),('c','e'),('g','h'),('h','e'),('g','j'),('f','g')]

graph = Graph(edges)

visited = []
print('DFS')
dfs(visited,graph,'i')
print()
