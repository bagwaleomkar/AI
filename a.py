graph = {
 'a': [('b',4), ('c',3)],
 'b': [('e',12), ('f',5)],
 'c': [('d',7), ('e',10)],
 'd': [('e',2)],
 'e': [('z',5)],
 'f': [('z',16)],
 'z': []
}

h = {
 'a':14,
 'b':12,
 'c':11,
 'd':6,
 'e':4,
 'f':11,
 'z':0
}

def a_star(start, goal):

    open_list = [(start, 0)]

    visited = []

    while open_list:

        # Find minimum f(n)
        current, cost = min(open_list,
                            key=lambda x: x[1] + h[x[0]])

        open_list.remove((current, cost))

        print("Visited:", current)

        if current == goal:

            print("Goal Reached")

            print("Minimum Cost =", cost)

            break

        visited.append(current)

        # Add neighbors
        temp = []

        for neigh, weight in graph[current]:

            if neigh not in visited:

                temp.append((neigh, cost + weight))

        # Keep only best nodes
        open_list = temp

# Main
a_star('a', 'z')
