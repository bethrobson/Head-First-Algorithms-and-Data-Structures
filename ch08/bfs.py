# Breadth First Shortest Path

from queue import Queue

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

def bfs(graph, start, goal):
    visited = set()
    queue = Queue([(start, [start])])

    while not queue.isEmpty():
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

print("--- Shortest Path from Ticket Counter to ED ---")
path = bfs(algorithmland, "TC", "ED")
print(f"ED: {path}")

