from algos.bidirectional_search import bidirectional_search
from algos.breadth_first_search import breadth_first_search
from algos.depth_first_search import depth_first_search
from algos.depth_iterative_search import depth_iterative_search
from algos.depth_limit_search import depth_limit_search
from algos.greedy_search_first_best_match import greedy_search_first_best_match
from algos.total_assessment_minimization_search import total_assessment_minimization_search
from model import graph, node_index, end_city, begin_city
from utils.graph_utils import draw_graph
from utils.io_utils import read_graph, convert_result_to_names

read_graph()
draw_graph('graph')

# 1 step
result_bfs = convert_result_to_names(breadth_first_search(graph, node_index[begin_city], node_index[end_city]))
print("Поиск в ширину: ", result_bfs)
draw_graph('bfs', result_bfs)

result_dfs = convert_result_to_names(depth_first_search(graph, node_index[begin_city], node_index[end_city]))
print("Поиск в глубину: ", result_dfs)
draw_graph('dfs', result_dfs)

result_dls = convert_result_to_names(depth_limit_search(graph, node_index[begin_city], node_index[end_city], 8))
print("Поиск с ограничением глубины: ", result_dls)
draw_graph('dls', result_dls)

result_dis = convert_result_to_names(depth_iterative_search(graph, node_index[begin_city], node_index[end_city]))
print("Поиск с итеративным углублением: ", result_dis)
draw_graph('dis', result_dis)

result_bidirect = convert_result_to_names(bidirectional_search(graph, node_index[begin_city], node_index[end_city]))
print("Двунаправленный поиск: ", result_bidirect)
draw_graph('bi-direct', result_bidirect)

# 2 step
result_greedy = convert_result_to_names(greedy_search_first_best_match(graph, node_index[begin_city], node_index[end_city]))
print("Жадный поиск по первому наилучшему соответствию: ", result_greedy)
draw_graph('greedy', result_greedy)

result_a = convert_result_to_names(total_assessment_minimization_search(graph, node_index[begin_city], node_index[end_city]))
print("Метод минимизации суммарной оценки стоимости решения:", result_a)
draw_graph('a', result_a)

