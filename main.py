import numpy as np
from convert import *
from DFS import *
from BFS import *
from UCS import *

# Helper method used to set all values in visited to False
# param_1: visited: dict[str: bool]
# return:


def resetVisited(visited: dict[str: bool]):
    for keys in visited:
        visited[keys] = False
    return


visited = {'S': False,
           'A': False,
           'B': False,
           'C': False,
           'D': False,
           'E': False,
           'F': False,
           'H': False,
           'P': False,
           'Q': False,
           'R': False,
           'G': False}

matrix_1 = np.zeros((12, 12), dtype=int)
matrix_2 = np.zeros((12, 12), dtype=int)
matrix_3 = np.zeros((12, 12), dtype=int)
matrix_4 = np.zeros((12, 12), dtype=int)

vertex_list_1_3 = {'S': ['D', 'E', 'P'],
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

edge_list_3 = {'S': [3, 9, 1],
               'A': [2, 2],
               'B': [2, 1],
               'C': [2, 8, 3],
               'D': [1, 8, 2, 3],
               'E': [2, 8, 2, 9],
               'F': [3, 2, 2],
               'H': [8, 4, 4],
               'P': [4, 15, 1],
               'Q': [4, 15],
               'R': [2, 2],
               'G': [2]}

vertex_list_2_4 = {'S': ['D', 'E', 'P'],
                   'B': ['A'],
                   'C': ['A'],
                   'D': ['B', 'C', 'E'],
                   'E': ['H', 'R'],
                   'F': ['C', 'G'],
                   'H': ['P', 'Q'],
                   'P': ['Q'],
                   'R': ['F']}

edge_list_4 = {'S': [3, 9, 1],
               'B': [2],
               'C': [2],
               'D': [1, 8, 2],
               'E': [8, 2],
               'F': [3, 2],
               'H': [4, 4],
               'P': [15],
               'R': [2]}

matrix_1 = convert.convertListToMatrixUW(matrix_1, vertex_list_1_3)
matrix_2 = convert.convertListToMatrixUW(matrix_2, vertex_list_2_4)
matrix_3 = convert.convertListToMatrixW(matrix_3, vertex_list_1_3, edge_list_3)
matrix_4 = convert.convertListToMatrixW(matrix_4, vertex_list_2_4, edge_list_4)

# Graph 1: DFS/ BFS Iterative and Recursive using vertex list
print("\n\nGraph 1: DFS Stack Recursively VertexList")
print(f"Path returned states:", end=" ")
DFS.DFS_stack_recursive_v('S', 'G', vertex_list_1_3, visited)
print(f"\nPath expanded states: {DFS.searchPath}")
resetVisited(visited)
DFS.empty()

print("\n\nGraph 1: DFS Stack Iteratively VertexList")
print(f"Path returned states:", end=" ")
DFS.DFS_stack_iterative_v('S', vertex_list_1_3, visited)
print(f"\nPath expanded states: {DFS.searchPath}")
resetVisited(visited)
DFS.empty()

print("\n\nGraph 1: BFS Queue Recursive VertexList")
print(f"Path returned states:", end=" ")
BFS.BFS_queue_recursive_v('S', vertex_list_1_3, visited)
print(f"\nPath expanded states: {BFS.searchPath}")
resetVisited(visited)
BFS.empty()

print("\n\nGraph 1: BFS Queue Iterative VertexList")
print(f"Path returned states:", end=" ")
BFS.BFS_queue_iterative_v('S', vertex_list_1_3, visited)
print(f"\nPath expanded states: {BFS.searchPath}")

resetVisited(visited)
BFS.empty()

print("\n____________________________________________________", end=" ")

# Graph 1: DFS/ BFS Iterative and Recursive using adjacency matrix
print("\n\nGraph 1: DFS Stack Recursively Adjacency Matrix")
print(f"Path returned states:", end=" ")
DFS.DFS_stack_recursive_adj(11, 6, matrix_1, visited)
print(f"\nPath expanded states: {DFS.searchPath}")
resetVisited(visited)
DFS.empty()

print("\n\nGraph 1: DFS Stack Iterative Adjacency Matrix")
print(f"Path returned states:", end=" ")
DFS.DFS_stack_iterative_adj(11, matrix_1, visited)
print(f"\nPath expanded states: {DFS.searchPath}")
resetVisited(visited)
DFS.empty()

print("\n\nGraph 1: BFS Queue Recursive Adjacency Matrix")
print(f"Path returned states:", end=" ")
BFS.BFS_queue_recursive_adj(11, matrix_1, visited)
print(f"\nPath expanded states: {BFS.searchPath}")
resetVisited(visited)
BFS.empty()

print("\n\nGraph 1: BFS Queue Iterative Adjacency Matrix")
print(f"Path returned states:", end=" ")
BFS.BFS_queue_iterative_adj(11, matrix_1, visited)
print(f"\nPath expanded states: {BFS.searchPath}")
resetVisited(visited)
BFS.empty()

print("\n____________________________________________________", end=" ")

# Graph 2: DFS/ BFS Iterative and Recursive using vertex list
print("\n\nGraph 2: DFS Stack Recursively VertexList")
print(f"Path returned states:", end=" ")
DFS.DFS_stack_recursive_v('S', 'G', vertex_list_2_4, visited)
print(f"\nPath expanded states: {DFS.searchPath}")
resetVisited(visited)
DFS.empty()

print("\n\nGraph 2: DFS Stack Iteratively VertexList")
print(f"Path returned states:", end=" ")
DFS.DFS_stack_iterative_v('S', vertex_list_2_4, visited)
print(f"\nPath expanded states: {DFS.searchPath}")
resetVisited(visited)
DFS.empty()

print("\n\nGraph 2: BFS Queue Recursive VertexList")
print(f"Path returned states:", end=" ")
BFS.BFS_queue_recursive_v('S', vertex_list_2_4, visited)
print(f"\nPath expanded states: {BFS.searchPath}")
resetVisited(visited)
BFS.empty()

print("\n\nGraph 2: BFS Queue Iterative VertexList")
print(f"Path returned states:", end=" ")
BFS.BFS_queue_iterative_v('S', vertex_list_2_4, visited)
print(f"\nPath expanded states: {BFS.searchPath}")
resetVisited(visited)
BFS.empty()

print("\n____________________________________________________", end=" ")

# Graph 2: DFS/ BFS Iterative and Recursive using adjacency matrix
print("\n\nGraph 2: DFS Stack Recursively Adjacency Matrix")
print(f"Path returned states:", end=" ")
DFS.DFS_stack_recursive_adj(11, 6, matrix_2, visited)
print(f"\nPath expanded states: {DFS.searchPath}")
resetVisited(visited)
DFS.empty()

print("\n\nGraph 2: DFS Stack Iterative Adjacency Matrix")
print(f"Path returned states:", end=" ")
DFS.DFS_stack_iterative_adj(11, matrix_2, visited)
print(f"\nPath expanded states: {DFS.searchPath}")
resetVisited(visited)
DFS.empty()

print("\n\nGraph 2: BFS Queue Recursive Adjacency Matrix")
print(f"Path returned states:", end=" ")
BFS.BFS_queue_recursive_adj(11, matrix_2, visited)
print(f"\nPath expanded states: {BFS.searchPath}")
resetVisited(visited)
BFS.empty()

print("\n\nGraph 2: BFS Queue Iterative Adjacency Matrix")
print(f"Path returned states:", end=" ")
BFS.BFS_queue_iterative_adj(11, matrix_2, visited)
print(f"\nPath expanded states: {BFS.searchPath}")
resetVisited(visited)
BFS.empty()

print("\n____________________________________________________", end=" ")

print("\nGraph 3: UCS Iterative Vertex List")
print(f"Path returned states:", end=" ")
UCS.UCS_vertex_list('S', 'G', vertex_list_1_3, edge_list_3, visited)
print(f"\nPath expanded states:")
resetVisited(visited)

print("\nGraph 3: UCS Iterative Adjacency Matrix")
print(f"Path returned states:", end=" ")
UCS.UCS_adj_matrix(11, 6, matrix_3, visited)
print(f"\nPath expanded states: ")
resetVisited(visited)

print("\nGraph 4: UCS Iterative Vertex List")
print(f"Path returned states:", end=" ")
UCS.UCS_vertex_list('S', 'G', vertex_list_2_4, edge_list_4, visited)
print(f"\nPath expanded states: ")
resetVisited(visited)

print("\nGraph 4: UCS Iterative Adjacency Matrix")
print(f"Path returned states:", end=" ")
UCS.UCS_adj_matrix(11, 6, matrix_4, visited)
print(f"\nPath expanded states: ")
