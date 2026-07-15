def find(parent, node):
    if parent[node] == node:
        return node
    return find(parent, parent[node])

def union(parent, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        parent[root_v] = root_u
        return True
    return False

def kruskal(V,edges):
    edges = sorted(edges, key=lambda x: x[2])

    parent = list(range(V))
    

    mst = []
    total_cost = 0

    for u,v,w in edges:
        if union(parent,u, v):
            mst.append((u,v,w))
            total_cost += w
    return mst, total_cost


vertices = 5
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]   
mst, cost = kruskal(vertices, edges)
print("Edges in the Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} --> {v} = {w}")
print("Total Cost:", cost)


