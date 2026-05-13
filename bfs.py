graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# DFS using Recursion
visited = set()

def dfs(node):

    if node not in visited:

        print(node, end=" ")

        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

# BFS using Queue
def bfs(start):

    visited = []
    queue = [start]

    visited.append(start)

    while queue:

        node = queue.pop(0)

        print(node, end=" ")

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.append(neighbor)

                queue.append(neighbor)

# Main Program
print("DFS Traversal:")
dfs('A')

print("\n")

print("BFS Traversal:")
bfs('A')
