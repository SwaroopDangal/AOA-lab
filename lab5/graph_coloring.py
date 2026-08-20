def is_safe(graph, color, vertex, c):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n

    def solve(vertex):
        if vertex == n:
            print("Valid Coloring Found:")
            for i in range(n):
                print(f"Vertex {i+1} --> Color {color[i]}")
            return

        for c in range(1, m + 1):
            if is_safe(graph, color, vertex, c):
                color[vertex] = c
                solve(vertex + 1)
                color[vertex] = 0      # Backtrack

    solve(0)


# Example graph
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3
graph_coloring(graph, m)