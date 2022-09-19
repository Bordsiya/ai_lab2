from queue import PriorityQueue

from model import paths_straight, node_names


def backtrace(parent, start_node, end_node):
    path = [end_node]
    while path[-1] != start_node:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def total_assessment_minimization_search(graph, start, end):
    parent = {}
    used = [0] * len(graph)
    pq = PriorityQueue()
    pq.put((0, start))
    used[start] = 1
    while pq.not_empty:
        node_pair = pq.get()
        node = node_pair[1]
        sum = node_pair[0]
        #print(node_names[node], end=": ")
        if node == end:
            return backtrace(parent, start, end)
        for neighbour in graph[node]:
            to_node = neighbour[0]
            if used[to_node] == 0:
                #print(node_names[to_node], end=" ")
                parent[to_node] = node
                used[to_node] = 1
                path_direct = paths_straight[node_names[to_node]]
                pq.put((sum + neighbour[1] + path_direct, to_node))
        #print('')
    return []
