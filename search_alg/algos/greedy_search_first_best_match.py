from queue import PriorityQueue


def backtrace(parent, start_node, end_node):
    path = [end_node]
    while path[-1] != start_node:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def greedy_search_first_best_match(graph, start, end):
    parent = {}
    used = [0] * len(graph)
    pq = PriorityQueue()
    pq.put((0, start))
    used[start] = 1
    while pq.not_empty:
        node = pq.get()[1]
        # print(node_names[node], end=": ")
        if node == end:
            return backtrace(parent, start, end)
        for neighbour in graph[node]:
            to_node = neighbour[0]
            if used[to_node] == 0:
                # print(node_names[to_node], end=" ")
                parent[to_node] = node
                used[to_node] = 1
                pq.put((neighbour[1], to_node))
        # print('')
    return []