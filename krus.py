edges = [
 (4, 0, 1),
 (8, 0, 7),
 (11, 1, 7),
 (8, 1, 2),
 (7, 2, 3),
 (2, 2, 8),
 (4, 2, 5),
 (9, 3, 4),
 (14, 3, 5),
 (10, 4, 5),
 (2, 5, 6),
 (1, 6, 7),
 (6, 6, 8),
 (7, 7, 8)
]

# Sort edges
edges.sort()

parent = []

for i in range(9):
    parent.append(i)

def find(i):

    while parent[i] != i:
        i = parent[i]

    return i

def union(x, y):

    parent[x] = y

print("Edge : Weight")

for w, u, v in edges:

    x = find(u)
    y = find(v)

    if x != y:

        print(u, "-", v, ":", w)

        union(x, y)
