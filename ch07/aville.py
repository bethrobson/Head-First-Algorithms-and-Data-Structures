algorithmville = {
    "A": [("C", 2)],
    "C": [("M", 1)],
    "P": [("A", 2), ("S", 3)],
    "M": [("P", 0.5), ("L", 1), ("K", 5)],
    "L": [("M", 1)],
    "S": [("P", 3)],
    "K": [("M", 5)]
}

def neighbors(graph, vertex):
    result = []
    for edge in graph.get(vertex, []):
        neighbor = edge[0]
        result.append(neighbor)
    return result

print(f"Neighbors of M: {neighbors(algorithmville, 'M')}")
print(f"Neighbors of P: {neighbors(algorithmville, 'P')}")

def route_cost(graph, path):
    total = 0
    for i in range(len(path) - 1):
        v1 = path[i]
        v2 = path[i + 1]
        for neighbor, cost in graph.get(v1, []):
            if neighbor == v2:
                total += cost
                break
        else:
            print(f"No road from {v1} to {v2}")
            return None
    return total

print(f"A C M L: {route_cost(algorithmville, ['A', 'C', 'M', 'L'])}")
print(f"M P S: {route_cost(algorithmville, ['M', 'P', 'S'])}")
print(f"A P: {route_cost(algorithmville, ['A', 'P'])}")


