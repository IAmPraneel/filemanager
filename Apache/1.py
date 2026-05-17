graph = {}

n = int(input("Enter number of vertices"))

for i in range(n):
    node = input("enter vertex name: ").strip()
    neighbours_input = input("Enter neighbour nodes seperated by space").split()
    graph[node] = neighbours_input

def dfs(graph, node, visited = None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, " ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return(visited)

def bfs(graph, start):
    visited = set()
    queue = []
    queue.append(start)
    while len(queue) >0:
        node = queue.pop(0)
        if node not in visited:
            print(node," ")
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    queue.append(n)
    return(visited)

start_node = input("Enter start node: ").strip()

print("DFS: ",dfs(graph,start_node))
print("BFS: ",bfs(graph, start_node))
