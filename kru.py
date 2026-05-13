graph = {
 'A': {'B':4, 'C':5},
 'B': {'A':4, 'C':11, 'D':9, 'E':7},
 'C': {'A':5, 'B':11, 'E':3},
 'D': {'B':9, 'E':13, 'F':2},
 'E': {'B':7, 'C':3, 'D':13, 'F':6},
 'F': {'D':2, 'E':6}
}

# Distance dictionary
distance = {}

# Initialize distances
for node in graph:
    distance[node] = 999

# Starting node
start = 'A'

distance[start] = 0

visited = []

while len(visited) < len(graph):

    # Find minimum distance node
    min_node = None

    for node in graph:

        if node not in visited:

            if min_node is None or distance[node] < distance[min_node]:

                min_node = node

    visited.append(min_node)

    # Update distances
    for neighbor, weight in graph[min_node].items():

        if distance[min_node] + weight < distance[neighbor]:

            distance[neighbor] = distance[min_node] + weight

# Print shortest distances
print("Shortest Distance from A")

for node in distance:

    print(node, "=", distance[node])


































































