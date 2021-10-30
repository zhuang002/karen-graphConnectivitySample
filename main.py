def add_path(node1, node2, g):
    g[node1][node2] = 1
    g[node2][node1] = 1


def create_graph():
    n = 13
    graph = []
    for i in range(n):
        row = []
        graph.append(row)
        for j in range(n):
            row.append(0)

    add_path(0, 1, graph)
    add_path(0, 2, graph)
    add_path(1, 5, graph)
    add_path(1, 6, graph)
    add_path(1, 7, graph)
    add_path(2, 3, graph)
    add_path(2, 4, graph)
    add_path(2, 7, graph)
    add_path(2, 8, graph)
    add_path(7, 8, graph)
    add_path(9, 10, graph)
    add_path(9, 12, graph)
    add_path(10, 11, graph)
    add_path(11, 12, graph)

    # add_path(4, 9, graph)
    return graph


def get_new_neighbors(node, g, expended_nodes):
    new_neighbors = []
    n = len(g)
    for i in range(n):
        if g[node][i] == 1 and i not in expended_nodes:
            new_neighbors.append(i)
    return new_neighbors


def is_connected_graph(g):
    expended_nodes = [0]
    current_new_nodes = [0]
    next_new_nodes = []

    while current_new_nodes:
        for node in current_new_nodes:
            neighbors = get_new_neighbors(node, graph, expended_nodes)
            next_new_nodes.extend(neighbors)
            expended_nodes.extend(neighbors)

        current_new_nodes = next_new_nodes
        next_new_nodes = []

    n = len(graph)
    for i in range(n):
        if i not in expended_nodes:
            return False
    return True


graph = create_graph()
if is_connected_graph(graph):
    print("is connected")
else:
    print("is not connected")
