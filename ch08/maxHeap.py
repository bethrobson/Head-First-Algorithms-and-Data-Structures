# Max heap

import heapq

algorithmland = {
    "TC": [("VE", 3), ("LS", 2), ("FF", 2)],
    "VE": [("TC", 3), ("LL", 7), ("QT", 4)],
    "LL": [("VE", 7)],
    "LS": [("TC", 2), ("QT", 2), ("SS", 5)],
    "QT": [("VE", 4), ("LS", 2)],
    "FF": [("TC", 2), ("SS", 1)],
    "SS": [("HD", 4), ("LS", 5), ("FF", 1), ("ED", 3)],
    "HD": [("SS", 4), ("ED", 3)],
    "ED": [("HD", 3), ("SS", 3)]
}

# Find a long path by using a max-heap
def long_path(graph, start, goal):
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start, [start]))

    while pq:
        # print(f"Queue: { pq }")
        neg_cost, node, path = heapq.heappop(pq)
        cost = -neg_cost
        if node == goal:
            return path, cost
        if node in visited:
            continue
        print(f"Visiting {node} (cost {cost})")
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_cost = cost + weight
                heapq.heappush(pq, (-new_cost, neighbor, path + [neighbor]))
    return None, float("-inf")

start = "TC"
goal = "ED"
print(f"--- A long path using a max-heap from {start} to {goal} ---")
path, cost  = long_path(algorithmland, start, goal)
print(f"Cost for path {path} is { cost }")



