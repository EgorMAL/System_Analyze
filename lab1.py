import pandas as pd
import sys
import csv

def get_cell_by_index(path: str, x: int, y: int):
    df = pd.read_csv(path)
    return df.iloc[[x, y]]
# РАСКОММЕНТИРОВАТЬ ДЛЯ ЗАДАНИЯ 1
# path, x, y, = sys.argv[1:]
# print(get_cell_by_index(path, x, y))

def read_graph(path='graph.csv'):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

# РАСКОММЕНТИРОВАТЬ ДЛЯ ЗАДАНИЯ 2
# data = read_graph()
# for i in range(8):
#     neighbours = []
#     for j in range(8):
#         if data[i][j] == '1':
#             neighbours.append(str(j))
#     print(f"Вершина {i} соединяется с вершинами {', '.join(neighbours)}")