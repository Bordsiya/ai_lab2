used = []
parent = {}
start_node = None
end_node = None


def backtrace():
    path = [end_node]
    while path[-1] != start_node:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def dls(graph, node, path, level, limit):
    used[node] = 1
    path.append(node)
    if node == end_node:
        return backtrace()
    if level == limit:
        return False
    for neighbour in graph[node]:
        to_node = neighbour[0]
        if used[to_node] == 0:
            parent[to_node] = node
            if dls(graph, to_node, path, level + 1, limit):
                return backtrace()
    path.pop()
    return False


def depth_limit_search(graph, start, end, limit):
    global used
    global start_node
    global end_node
    used = [0] * len(graph)
    start_node = start
    end_node = end
    result = dls(graph, start, [], 0, limit)
    if not result:
        return []
    else:
        return result
