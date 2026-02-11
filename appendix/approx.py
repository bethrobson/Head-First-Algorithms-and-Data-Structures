
# Vertex Cover
# Find the smallest set of vertices such that every edge
# has at least one endpoint in that set.

# Algorithm
# 1. Pick any edge (u, v)
# 2. Add both u and v to the cover
# 3. Remove all edges covered by u or v
# 4. Repeat until all edges are covered

# This is a "2-approximation" algorithm because the size
# of this cover is less than or equal twice the optimal solution.

def approx_vertex_cover(edges):
    cover = set()
    edges = edges.copy()
    while edges:
        u, v = edges.pop()
        cover.add(u)
        cover.add(v)
        # remove edges covered by u or v (no guaranteed order!)
        edges = [ (a,b) for a,b in edges if a not in cover and b not in cover ]
    return cover

edge_list = [('VE', 'LL'), ('HD', 'ED'), ('QT', 'LS'), ('TC', 'VE'), ('SS', 'ED'), ('TC', 'FF'), ('LS', 'SS'), ('QT', 'VE'), ('TC', 'LS'), ('FF', 'SS'), ('HD', 'SS')]

cover = approx_vertex_cover(edge_list)
print("Approximate vertex cover:", cover)

# Note you can get a slightly different result each time
# because cover is a set so checking for edges in the set
# doesn't guarantee an ordering.

