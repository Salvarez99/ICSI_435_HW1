import numpy as np

class convert:
    letters = np.array(["S", "A", "B", "C", "D", 'E', 'F', 'H', 'P', 'Q', 'R', 'G'])
    vertices = {'S' : 0,
                'A' : 1,
                'B' : 2,
                'C' : 3,
                'D' : 4,
                'E' : 5,
                'F' : 6,
                'H' : 7,
                'P' : 8,
                'Q' : 9,
                'R' : 10,
                'G' : 11}
    matrix: np.ndarray
    vertex_list: dict[str, list[str]]

    def __init__(self,matrix: np.ndarray, vertex_list: dict[str, list[str]]):

        self.matrix = matrix
        self.vertex_list = vertex_list

        return 

    def convertListToMatrixUW(self):
        for key, values in self.vertex_list.items():    
            if key in self.vertices:
                row = self.vertices.get(key)
                for value in values:
                    col = self.vertices.get(value)
                    self.matrix[row][col] = 1

        return self.matrix

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
