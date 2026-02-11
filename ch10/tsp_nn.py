# Traveling Salesman, Nearest Neighbor

def tsp_nearest_neighbor(cities, dist, start=0):
    n = len(cities)
    visited = [False] * n
    path = [start]
    visited[start] = True
    total_distance = 0
    current = start

    for _ in range(n - 1):
        next_city = None
        min_dist = float("inf")

        for i in range(n):
            if not visited[i] and dist[current][i] < min_dist:
                min_dist = dist[current][i]
                next_city = i

        path.append(next_city)
        visited[next_city] = True
        total_distance += min_dist
        current = next_city

    # return to start
    total_distance += dist[current][start]
    path.append(start)

    named_path = [cities[i] for i in path]
    return named_path, total_distance

cities = [
    "Austin",
    "Orlando",
    "Boca Chica",
    "Santa Fe",
    "Las Vegas"
]

dist = [
    # AUST  ORL   BOCA  SFE   LV
    [   0, 1100,  350,  700, 1200],  # Austin
    [1100,    0, 1350, 1800, 2250],  # Orlando
    [ 350, 1350,    0,  900, 1150],  # Boca Chica
    [ 700, 1800,  900,    0,  650],  # Santa Fe
    [1200, 2250, 1150,  650,    0]   # Las Vegas
]

path, total = tsp_nearest_neighbor(cities, dist, start=0)
print("Route:", " → ".join(path))
print("Total miles:", total)


