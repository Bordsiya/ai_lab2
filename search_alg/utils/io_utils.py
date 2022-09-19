import traceback

from model import graph, node_names, node_index


def read_graph_file(file_name):
    try:
        file = open(file_name, encoding='utf-8', mode='r')
        lines = file.readlines()
        for line in lines:
            city1, city2, path_len = line.strip().split(" ")
            if city1 not in node_names:
                node_names.append(city1)
                node_index[city1] = len(node_names) - 1
            if city2 not in node_names:
                node_names.append(city2)
                node_index[city2] = len(node_names) - 1
            graph[node_index[city1]].append((node_index[city2], int(path_len)))
            graph[node_index[city2]].append((node_index[city1], int(path_len)))
    except ValueError:
        print(traceback.format_exc())
        file.close()
        exit(1)
    except FileNotFoundError or IOError:
        print(traceback.format_exc())
        exit(1)

    file.close()


def read_graph_console():
    print('Введите список вершин:')
    while True:
        try:
            city1, city2, path_len = input().split(" ")
            if city1 not in node_names:
                node_names.append(city1)
                node_index[city1] = len(node_names) - 1
            if city2 not in node_names:
                node_names.append(city2)
                node_index[city2] = len(node_names) - 1
            graph[node_index[city1]].append((node_index[city2], int(path_len)))
            graph[node_index[city2]].append((node_index[city1], int(path_len)))
        except ValueError:
            break


def read_graph():
    inp = input('Вы желаете ввести исходные данные из файла? y/n: ')

    if inp in ['Y', 'y']:
        file_name = input('Введите имя файла: ').strip()
        read_graph_file(file_name)
    elif inp in ['N', 'n']:
        read_graph_console()
    else:
        print(traceback.format_exc())
        exit(1)


def convert_result_to_names(result):
    converted_result = []
    for node in result:
        converted_result.append(node_names[node])
    return converted_result
