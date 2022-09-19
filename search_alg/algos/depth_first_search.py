
used = []
parent = {}
start_node = None
end_node = None
result = []


def backtrace():
    global result
    path = [end_node]
    while path[-1] != start_node:
        path.append(parent[path[-1]])
    path.reverse()
    result = path


def dfs(graph, curr_node):
    if curr_node == end_node:
        backtrace()
    used[curr_node] = 1
    # print(curr_node, end=": ")
    for neighbour in graph[curr_node]:
        to_node = neighbour[0]
        if used[to_node] == 0:
            # print(to_node)
            parent[to_node] = curr_node
            dfs(graph, to_node)


def depth_first_search(graph, start, end):
    global used
    global start_node
    global end_node
    used = [0] * len(graph)
    start_node = start
    end_node = end
    dfs(graph, start)
    return result
