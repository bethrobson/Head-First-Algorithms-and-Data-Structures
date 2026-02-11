# Breadth First Traversal and Shortest Path

from queue import Queue
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

# difficulty rating for the shortest path
def difficulty_for_path(graph, start, goal):
    visited = set()
    queue = Queue([(0, start, [start])]) 

    while not queue.isEmpty():
        # print(f"Queue: { queue }")
        difficulty, node, path = queue.pop()
        if node == goal:
            return difficulty, path
        if node in visited:
            continue
        print("Visiting ", node)
        visited.add(node)

        discovers = []
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                discovers.append((neighbor, difficulty + weight))
                queue.push((difficulty + weight, neighbor, path + [neighbor]))
        # print(f"Discovered: { discovers }")

    return float("inf"), None

start = "TC"
goal = "ED"
#print(f"--- Path from {start} to {goal} ---")
#difficulty, path = difficulty_for_path(algorithmland, start, goal)
#print(f"Difficulty for path {path} is {difficulty}")


def easiest_path(graph, start, goal):
    visited = set()
    heap = []
    heapq.heappush(heap, (0, start, [start]))

    while heap:
        difficulty, node, path = heapq.heappop(heap)

        if node == goal:
            return difficulty, path
        if node in visited:
            continue
        print("Visiting ", node)
        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (difficulty+weight, neighbor, path+[neighbor]))

    return float("inf"), None


start = "TC"
goal = "ED"
print(f"--- Easiest path with heap from {start} to {goal} ---")
difficulty, path = easiest_path(algorithmland, start, goal)
print(f"Difficulty for path {path} is {difficulty}")


def dijkstra(graph, start, goal):
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start, [start]))

    while pq:
        # print(f"Queue: { pq }")
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        if node in visited:
            continue
        print(f"Visiting {node} (cost {cost})")
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_cost = cost + weight
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
    return None, float("inf")

start = "TC"
goal = "ED"
print(f"--- Cheapest path using Dijkstra's algorithm from {start} to {goal} ---")
path, cost  = dijkstra(algorithmland, start, goal)
print(f"Cost for path {path} is { cost }")



