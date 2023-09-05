import numpy as np 

def printAdjMatrix(matrix: np.ndarray, vertices : np.ndarray):
    print("   ", end=" ")
    for i in range(vertices.size):
        print(f"{vertices[i]}", end=" ")

    print("\n")
    for rows in range(12):
        print(f"{vertices[rows]}: ", end=" ")
        for cols in range(12):
            print(f"{matrix[rows,cols]}", end=" ")
        print("\n")

    return

vertices = np.array(["S", "A", "B", "C", "D", 'E', 'F', 'H', 'P', 'Q', 'R', 'G'])
                            #S A B C D E F H P Q R G 
graph_1_adj_mat = np.array([(0,0,0,0,1,1,0,0,1,0,0,0), #S
                            (0,0,1,1,0,0,0,0,0,0,0,0), #A
                            (0,1,0,0,1,0,0,0,0,0,0,0), #B
                            (0,1,0,0,1,0,1,0,0,0,0,0), #C
                            (1,0,1,1,0,1,0,0,0,0,0,0), #D
                            (1,0,0,0,1,0,0,1,0,0,1,0), #E
                            (0,0,0,1,0,0,0,0,0,0,1,1), #F
                            (0,0,0,0,0,1,0,0,1,1,0,0), #H
                            (1,0,0,0,0,0,0,1,0,1,0,0), #P
                            (0,0,0,0,0,0,0,1,1,0,0,0), #Q
                            (0,0,0,0,0,1,1,0,0,0,0,0), #R
                            (0,0,0,0,0,0,1,0,0,0,0,0)])#G

printAdjMatrix(graph_1_adj_mat, vertices)

graph_1 = {'S' : ['D','E','P'],       #^
           'A' : ['B','C'],           #^ 
           'B' : ['A','D'],           #^ 
           'C' : ['A','D','F'],       #^      
           'D' : ['B','C','E','S'],   #^
           'E' : ['D','H','R','S'],   #^
           'F' : ['C','G','R'],       #^
           'H' : ['E','P','Q'],       #^
           'P' : ['H','Q','S'],       #^
           'Q' : ['H','P'],           #^
           'R' : ['E','F'],           #^
           'G' : ['F']}               #^

for vertex in range(12):
    print(vertices[vertex], ": ",graph_1[vertices[vertex]])
