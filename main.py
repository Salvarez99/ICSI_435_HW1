from convert import *
import numpy as np
import sys
sys.path.append(
    '/Users/xenep/OneDrive/Documents/UAlbany/Fall 2023/ICSI 435 AI/Alvarez_S_Homework1/convert.py')

matrix_1 = np.zeros((12, 12), dtype=int)
matrix_2 = np.zeros((12, 12), dtype=int)

graph_1 = {'S': ['D', 'E', 'P'],
           'A': ['B', 'C'],
           'B': ['A', 'D'],
           'C': ['A', 'D', 'F'],
           'D': ['B', 'C', 'E', 'S'],
           'E': ['D', 'H', 'R', 'S'],
           'F': ['C', 'G', 'R'],
           'H': ['E', 'P', 'Q'],
           'P': ['H', 'Q', 'S'],
           'Q': ['H', 'P'],
           'R': ['E', 'F'],
           'G': ['F']}

graph_2 = {'S': ['D', 'E', 'P'],
           'B': ['A'],
           'C': ['A'],
           'D': ['B', 'C', 'E'],
           'E': ['H', 'R'],
           'F': ['C', 'G'],
           'H': ['P', 'Q'],
           'P': ['Q'],
           'R': ['F']}

matrix_1 = convert.convertListToMatrixUW(matrix_1, graph_1)
matrix_2 = convert.convertListToMatrixUW(matrix_2, graph_2)

convert.printAdjMatrix(matrix_1)
print()
convert.printAdjMatrix(matrix_2)

