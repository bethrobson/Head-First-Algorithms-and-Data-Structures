# Breadth First Traversal and Shortest Path

from queue import Queue
from stack import Stack

algorithmland = {
    "TC": ["VE", "LS", "FF"],
    "VE": ["TC", "LL", "QT"],
    "LL": ["VE"],
    "LS": ["TC", "QT", "SS"],
    "QT": ["VE", "LS"],
    "FF": ["TC", "SS"],
    "SS": ["HD", "LS", "FF", "ED"],
    "HD": ["SS", "ED"],
    "ED": ["HD", "SS"]
}

def bft(graph, start):
    visited = set()
    queue = Queue([start])

    while not queue.isEmpty():
        # print(f"Queue: { queue }") # uncomment to see the queue at each step
        node = queue.pop()
        if node in visited:
            continue
        print("Visiting:", node)
        visited.add(node)
        for neighbor in graph[node]:
            if (neighbor not in visited):
                queue.push(neighbor)

print("--- Breadth First Traversal of Algorithm Land ---")
bft(algorithmland, "TC")

def shortest_path(graph, start, goal):
    visited = set()
    queue = Queue([(start, [start])])

    while not queue.isEmpty():
        print(f"Queue: { queue }") # uncomment to see the queue at each step
        node, path = queue.pop()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.push((neighbor, path + [neighbor]))
    return None

print("--- Shortest Path from Ticket Counter to various spots ---")
path = shortest_path(algorithmland, "TC", "QT")
print(f"QT: {path}")
path = shortest_path(algorithmland, "TC", "ED")
print(f"ED: {path}")
path = shortest_path(algorithmland, "TC", "HD")
print(f"HD: {path}")
path = shortest_path(algorithmland, "TC", "SS")
print(f"SS: {path}")

# Depth-first traversal of the whole graph
def dft(graph, start):
    visited = set()
    stack = Stack([start])

    while not stack.isEmpty():
        node = stack.pop()
        if node in visited:
            continue
        print("Visiting:", node)
        visited.add(node)
        for neighbor in graph[node]:
            if (neighbor not in visited):
                stack.push(neighbor)


print("--- Depth First Traversal of Algorithm Land ---")
dft(algorithmland, "TC")

# Depth-first search for specific goal 
def dfs(graph, start, goal):
    visited = set()
    stack = Stack([(start, [start])])

    while not stack.isEmpty():
        node, path = stack.pop()
        if node == goal:
            return path
        if node in visited:
            continue
        print("Visiting:", node)
        visited.add(node)
        for neighbor in graph[node]:
            if (neighbor not in visited):
                stack.push((neighbor, path + [neighbor]))
    return None

print("--- Depth First Path from Ticket Counter to Exponential Drop ---")
path = dfs(algorithmland, "TC", "ED")
print(path)

# Recursive implementation of DFS
def dfs_recursive(graph, node, goal, visited=None, path=None):
    if visited is None: visited = set()
    if path is None: path = [node]

    print("Visiting:", node)
    visited.add(node)

    # Base case: goal found
    if node == goal:
        return path

    # Recurse on neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dfs_recursive(graph, neighbor, goal, visited, path + [neighbor])
            if result:              # If the recursive call found the goal
                return result

    # If no path found from this branch
    return None

print("--- Recursive DFS from Ticket Counter to Exponential Drop ---")
path = dfs_recursive(algorithmland, "TC", "ED")
print(path)


# Breadth-first search for shortest path with adjacency matrix

matrix = [
    # TC  VE  LL  LS  QT  FF  SS  HD  ED
    [0,  1,  0,  1,  0,  1,  0,  0,  0],  # TC
    [1,  0,  1,  0,  1,  0,  0,  0,  0],  # VE
    [0,  1,  0,  0,  0,  0,  0,  0,  0],  # LL
    [1,  0,  0,  0,  1,  0,  1,  0,  0],  # LS
    [0,  1,  0,  1,  0,  0,  0,  0,  0],  # QT
    [1,  0,  0,  0,  0,  0,  1,  0,  0],  # FF
    [0,  0,  0,  1,  0,  1,  0,  1,  1],  # SS
    [0,  0,  0,  0,  0,  0,  1,  0,  1],  # HD
    [0,  0,  0,  0,  0,  0,  1,  1,  0],  # ED
]

def shortest_path_matrix(matrix, nodes, start, goal):
    visited = set()
    queue = Queue([(start, [start])])

    while not queue.isEmpty():
        node, path = queue.pop()
        if node == goal:
            steps = len(path) - 1
            return path, steps

        if node in visited:
            continue

        visited.add(node)
        node_index = nodes.index(node)

        # Look across the row for neighbors (1 means connected)
        # i is the index of the matrix entry,
        # edge is 0 or 1 depending on if there is an edge there
        for i, edge in enumerate(matrix[node_index]):
            if edge == 1:
                neighbor = nodes[i]
                if neighbor not in visited:
                    queue.push((neighbor, path + [neighbor]))

    return None, None

# The index of the vertex in the list matches the index in the matrix
nodes = ["TC", "VE", "LL", "LS", "QT", "FF", "SS", "HD", "ED"]

print("-- Shortest path from HD to TC using adjacency matrix --")
path, steps = shortest_path_matrix(matrix, nodes, "HD", "TC")
print(f"Shortest path from HD to TC: { path }")
print(f"Number of steps: { steps }")

