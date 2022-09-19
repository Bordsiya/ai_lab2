from model import node_names


def backtrace(parent_right, parent_left, node, start_node, end_node):
    path_left = [node]
    while path_left[-1] != end_node:
        path_left.append(parent_left[path_left[-1]])
    path_right = [node]
    while path_right[-1] != start_node:
        path_right.append(parent_right[path_right[-1]])
    path_right.reverse()
    path = path_right
    for elem in path_left[1:]:
        path.append(elem)
    return path


def bidirectional_search(graph, start_node, end_node):
    parent_right = {}
    parent_left = {}
    queue = [start_node, end_node]
    used_left = [0] * len(graph)
    used_right = [0] * len(graph)
    used_left[end_node] = 1
    used_right[start_node] = 1
    while queue:
        node = queue.pop(0)
        if used_right[node] == 1 and used_left[node] == 1:
            return backtrace(parent_right, parent_left, node, start_node, end_node)
        #print(node_names[node], end=": ")
        for neighbour in graph[node]:
            to_node = neighbour[0]
            if used_right[node] == 1 and used_right[to_node] == 0:
                #print("right", node_names[to_node], end=" ")
                parent_right[to_node] = node
                used_right[to_node] = 1
                queue.append(to_node)
            if used_left[node] == 1 and used_left[to_node] == 0:
                #print("left", node_names[to_node], end=" ")
                parent_left[to_node] = node
                used_left[to_node] = 1
                queue.append(to_node)
        #print('')
    return []
