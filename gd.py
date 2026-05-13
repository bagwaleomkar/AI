graph = { 
'A': ['B', 'C'], 
'B': ['D', 'E'], 
'C': ['F'], 
'D': [], 
'E': ['G'], 
'F': ['G'], 
'G': [] 
} 

# Heuristic values 
h = { 
'A': 5, 
'B': 4, 
'C': 2, 
'D': 6, 
'E': 3, 
'F': 1, 
'G': 0 
} 

def greedy(start, goal): 

    open_list = [start] 

    visited = [] 

    while open_list: 

        # Select node with minimum heuristic value 
        current = min(open_list, key=lambda x: h[x]) 

        open_list.remove(current) 

        print("Visited:", current) 

        if current == goal: 

            print("Goal Reached") 

            break 

        visited.append(current) 

        # Add neighbors 
        for neigh in graph[current]: 

            if neigh not in visited: 

                open_list.append(neigh) 

# Main 
greedy('A', 'G')
