import numpy as np
from convert import *
from DFS import *
from BFS import *

def resetVisited(visited : dict[str : bool]):
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

edge_list_3 = np.array([3,9,1,
                        2,2,
                        2,1,
                        2,8,3,
                        1,8,2,3,
                        2,8,2,9,
                        3,2,2,
                        8,4,4,
                        4,15,1,
                        4,15,
                        2,2,
                        2])

vertex_list_2_4 = {'S': ['D', 'E', 'P'],
                   'B': ['A'],
                   'C': ['A'],
                   'D': ['B', 'C', 'E'],
                   'E': ['H', 'R'],
                   'F': ['C', 'G'],
                   'H': ['P', 'Q'],
                   'P': ['Q'],
                   'R': ['F']}

edge_list_4 = np.array([3,9,1,
                        2,
                        2,
                        1,8,2,
                        8,2,
                        3,2,
                        4,4,
                        15,
                        2])

matrix_1 = convert.convertListToMatrixUW(matrix_1, vertex_list_1_3)
matrix_2 = convert.convertListToMatrixUW(matrix_2, vertex_list_2_4)
matrix_3 = convert.convertListToMatrixW(matrix_3, vertex_list_1_3, edge_list_3)
matrix_4 = convert.convertListToMatrixW(matrix_4, vertex_list_2_4, edge_list_4)

# print("Graph 1")
# convert.printAdjMatrix(matrix_1)
# print("\nGraph 2")
# convert.printAdjMatrix(matrix_2)
# print("\nGraph 3")
# convert.printAdjMatrix(matrix_3)
# print("\nGraph 4")
# convert.printAdjMatrix(matrix_4)

#Completed (2)
#DFS Stack It Vertex
print("Graph 1: DFS Stack Iteratively VertexList")
DFS.DFS_stack_iterative_v(vertex_list_1_3, visited)
resetVisited(visited)
print("\n\nGraph 2: DFS Stack Iteratively VertexList")
DFS.DFS_stack_iterative_v(vertex_list_2_4, visited)
resetVisited(visited)


#Completed (2)
#DFS Stack It Adj
print("\n\nGraph 1: DFS Stack Iterative Adjacency Matrix")
DFS.DFS_stack_iterative_adj(11, matrix_1, visited)
resetVisited(visited)
print("\n\nGraph 2: DFS Stack Iterative Adjacency Matrix")
DFS.DFS_stack_iterative_adj(11, matrix_2, visited)
resetVisited(visited)



# #Debugging (2)
# #DFS Stack Recursive Vertex
# print("\n\nGraph 1: DFS Stack Recursively VertexList")
# DFS.DFS_stack_recursive_v('S', 'G', vertex_list_1_3, visited)
# resetVisited(visited)
# print("\n\nGraph 2: DFS Stack Recursively VertexList")
# DFS.DFS_stack_recursive_v('S', 'G', vertex_list_2_4, visited)
# resetVisited(visited)

#WIP (2)
#DFS Stack Recursive Adj
print("\n\nGraph 1: DFS Stack Recursively Adjacency Matrix")
DFS.DFS_stack_recursive_adj(11, 6, matrix_1, visited)
resetVisited(visited)
print("\n\nGraph 2: DFS Stack Recursively Adjacency Matrix")
DFS.DFS_stack_recursive_adj(11, 6, matrix_2, visited)
resetVisited(visited)


# # #Completed (2)
# # #BFS Queue It VertexList
# print("\n\nGraph 1: BFS Queue Iterative VertexList")
# BFS.BFS_queue_iterative_v('S', vertex_list_1_3, visited)
# resetVisited(visited)
# print("\n\nGraph 2: BFS Queue Iterative VertexList")
# BFS.BFS_queue_iterative_v('S', vertex_list_2_4, visited)
# resetVisited(visited)

# # # #Completed (2)
# # #BFS Queue It adj
# print("\n\nGraph 1: BFS Queue Iterative Adjacency Matrix")
# BFS.BFS_queue_iterative_adj(11, matrix_1, visited)
# resetVisited(visited)
# print("\n\nGraph 2: BFS Queue Iterative Adjacency Matrix")
# BFS.BFS_queue_iterative_adj(11, matrix_2, visited)
# resetVisited(visited)

# # #Complete (2)
# # #BFS Queue Recursive VertexList
# print("\n\nGraph 1: BFS Queue Recursive VertexList")
# BFS.BFS_queue_recursive_v('S', vertex_list_1_3, visited)
# resetVisited(visited)
# print("\n\nGraph 2: BFSQueue Recursive VertexList")
# BFS.BFS_queue_recursive_v('S', vertex_list_2_4, visited)
# resetVisited(visited)

# # #Complete (2)
# # #BFS Queue Recursive Adjacency Matrix
# print("\n\nGraph 1: BFS Queue Recursive Adjacency Matrix")
# BFS.BFS_queue_recursive_adj(11, matrix_1, visited)
# resetVisited(visited)
# print("\n\nGraph 2: BFS Queue Recursive Adjacency Matrix")
# BFS.BFS_queue_recursive_adj(11, matrix_2, visited)
# resetVisited(visited)