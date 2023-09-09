import numpy as np


class convert:
    letters = np.array(['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'P', 'Q', 'R','S'])
    vertices = {
                'A': 0,
                'B': 1,
                'C': 2,
                'D': 3,
                'E': 4,
                'F': 5,
                'G': 6,
                'H': 7,
                'P': 8,
                'Q': 9,
                'R': 10,
                'S': 11}

    #Convert list to unweighted adjacency matrix
    @classmethod
    def convertListToMatrixUW(self, matrix: np.ndarray, vertex_list: dict[str, list[str]]):
        for key, values in vertex_list.items():
            if key in self.vertices:
                row = self.vertices.get(key)
                for value in values:
                    col = self.vertices.get(value)
                    matrix[row][col] = 1

        return matrix
    
    #Convert list to weighted adjacency matrix
    @classmethod
    def convertListToMatrixW(self, matrix: np.ndarray, vertex_list: dict[str, list[str]], edge_list: np.ndarray):

        edge_index : int = 0
        for key, values in vertex_list.items():
            if key in self.vertices:
                row = self.vertices.get(key)
                for value in values:
                    col = self.vertices.get(value)
                    matrix[row][col] = edge_list[edge_index]
                    edge_index += 1

        return matrix

    @classmethod
    def printAdjMatrix(self, matrix: np.ndarray):
        print("  ", end=" ")
        for i in range(self.letters.size):
            print(f"{self.letters[i]} ", end=" ")

        print()
        for rows in range(12):
            print(f"{self.letters[rows]}: ", end="")
            for cols in range(12):
                if matrix[rows][cols] < 10:
                    print(f"{matrix[rows,cols]} ", end=" ")
                else:
                    print(f"{matrix[rows,cols]}", end=" ")

            print()

        return