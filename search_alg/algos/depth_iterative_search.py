from algos.depth_limit_search import depth_limit_search


def depth_iterative_search(graph, start, end):
    max_limit = len(graph)
    for limit in range(1, max_limit + 1):
        # print(limit)
        result = depth_limit_search(graph, start, end, limit)
        if len(result) != 0:
            return result
