def read_input(filename):
    with open(filename, "r") as file:
        n, m, k = map(int, file.readline().split())
        graph = [[0] * n for _ in range(n)]

        for _ in range(m):
            u, v = map(int, file.readline().split())
            graph[u][v] = 1
            graph[v][u] = 1

    return n, k, graph

def is_safe(vertex, graph, colors, color):
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True

def graph_coloring_util(graph, k, colors, vertex, n):
    if vertex == n:
        return True

    for color in range(1, k + 1):
        if is_safe(vertex, graph, colors, color):
            colors[vertex] = color
            if graph_coloring_util(graph, k, colors, vertex + 1, n):
                return True
            colors[vertex] = 0  # Backtrack

    return False

def graph_coloring(filename):
    n, k, graph = read_input(filename)
    colors = [0] * n

    if graph_coloring_util(graph, k, colors, 0, n):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", colors)
    else:
        print(f"Coloring Not Possible with {k} Colors")

if __name__ == "__main__":
    graph_coloring("f:/AI/Labrepot/Input.txt")
