graph = [
#1 2 3 4 5 6
[0,2,0,1,4,0], # 1
[2,0,3,3,0,7], # 2
[0,3,0,5,0,8], # 3
[1,3,5,0,9,0], # 4
[4,0,0,9,0,0], # 5
[0,7,8,0,0,0] # 6
]

v = 6

selected = [False] * v

# Start from vertex 1
selected[0] = True

print("Edge : Weight")

for i in range(v - 1):

    minimum = 999
    x = 0
    y = 0

    for j in range(v):

        if selected[j]:

            for k in range(v):

                if not selected[k] and graph[j][k]:

                    if minimum > graph[j][k]:

                        minimum = graph[j][k]

                        x = j
                        y = k

    print(x + 1, "-", y + 1, ":", graph[x][y])

    selected[y] = True
