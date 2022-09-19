import networkx as nx
import matplotlib.pyplot as plt

from model import graph, begin_city, end_city, node_names, node_index, graph_positions


def draw_graph(file_name, path=[]):
    edge_path = []
    if len(path) != 0:
        pred = path[0]
        for i in range(1, len(path)):
            edge_path.append((pred, path[i]))
            edge_path.append((path[i], pred))
            pred = path[i]

    G = nx.DiGraph()
    for city1_ind in graph:
        for city2 in graph[city1_ind]:
            city2_ind = city2[0]
            path_len = city2[1]
            G.add_edges_from([(node_names[city1_ind], node_names[city2_ind])], weight=path_len)
    node_colors = []
    for city in G.nodes():
        if city != begin_city and city != end_city:
            node_colors.append('lightskyblue')
        else:
            node_colors.append('salmon')
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    edge_colors = ['red' if edge in edge_path else 'black' for edge in G.edges]

    pos = nx.spring_layout(G, fixed=graph_positions.keys(), pos=graph_positions)
    plt.figure()
    plt.title(file_name)
    nx.draw(G, pos, node_color=node_colors, edge_color=edge_colors, arrows=False)
    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=6)
    plt.savefig(f'{file_name}')
    plt.show()
