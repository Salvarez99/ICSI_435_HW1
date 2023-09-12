import numpy as np


class DFS:

    stack = []

    vertices = {0: 'A',
                1: 'B',
                2: 'C',
                3: 'D',
                4: 'E',
                5: 'F',
                6: 'G',
                7: 'H',
                8: 'P',
                9: 'Q',
                10: 'R',
                11: 'S'}

    @classmethod
    def DFS_stack_iterative_v(self, vertex_list: dict[str, list[str]], visited: dict[str: bool]):

        key, value = next(iter(vertex_list.items()))
        node = {}
        node[key] = value

        self.stack.append(node)

        while not self.isEmpty(self):

            popped: dict[str, list[str]] = self.stack.pop()

            popped_key = list(popped.keys())[0]
            values = popped[popped_key]

            print(f"->{popped_key}", end="")

            # Checking if currentNode is the goal node
            if popped_key == 'G':
                return vertex_list.get(popped_key)

            # Iterate through each neighboring node
            # Check values is empty
            if values:
                for i in reversed(values):
                    if visited.get(i) == False:
                        visited[i] = True

                        nextNode = {}
                        nextNode[i] = vertex_list.get(i)

                        self.stack.append(nextNode)

        return 0

    @classmethod
    def DFS_stack_iterative_adj(self, start: int, adj_matrix: np.ndarray, visited: dict[str: bool]):
        self.stack = [start]

        while not self.isEmpty(self):
            node = self.stack.pop()
            print(f"->{self.vertices.get(node)}", end="")

            if node == 6:
                return node

            for col in reversed(range(len(adj_matrix))):
                node_key = self.vertices.get(col)

                if adj_matrix[node][col] == 1 and visited.get(node_key) == False:
                    visit = self.vertices.get(col)
                    visited[visit] = True

                    self.stack.append(col)

        return

    # WIP, ask TA for help
    # Desired output should be ->S->D->B->A->C->F->G
    @classmethod
    def DFS_stack_recursive_v(self, startNode: str, goalNode: str, vertex_list: dict[str, list[str]], visited: dict[str: bool] ):
        visited[startNode] = True
        print(f"->{startNode}", "")

        if startNode == goalNode:
            return True
        
        neighbors = vertex_list.get(startNode)

        if neighbors:
            for neighbor in neighbors:
                if visited.get(neighbor) == False:
                    if self.DFS_stack_recursive_v(neighbor,goalNode, vertex_list, visited):
                        return True

        return False


    # WIP
    @classmethod
    def DFS_stack_recursive_adj(self, startNode: int, goalNode: int, adj_matrix: np.ndarray, visited: dict[str: bool] ):
        nodeLetter = self.vertices.get(startNode)
        visited[nodeLetter] = True
        print(f"->{nodeLetter}", "")

        if startNode == goalNode:
            return True

        for col in range(len(adj_matrix)):
            neighborLetter = self.vertices.get(col)

            if adj_matrix[startNode][col] == 1 and visited.get(neighborLetter) == False:
                    if self.DFS_stack_recursive_adj(col, goalNode, adj_matrix, visited):
                        return True

        return False

    def isEmpty(self):
        if len(self.stack) == 0:
            return True

        return False
