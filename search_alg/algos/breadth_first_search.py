from model import node_names


def backtrace(parent, start_node, end_node):
    path = [end_node]
    while path[-1] != start_node:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def breadth_first_search(graph, start_node, end_node):
    parent = {}
    queue = [start_node]
    used = [0] * len(graph)
    used[start_node] = 1
    while queue:
        node = queue.pop(0)
        if node == end_node:
            return backtrace(parent, start_node, end_node)
        # print(node_names[node], end=": ")
        for neighbour in graph[node]:
            to_node = neighbour[0]
            if used[to_node] == 0:
                # print(node_names[to_node], end=" ")
                parent[to_node] = node
                used[to_node] = 1
                queue.append(to_node)
        # print('')
    return []
