import numpy as np


class DFS:

    stack = []

    vertices = {0 :'A',
                1 :'B',
                2 :'C',
                3 :'D',
                4 :'E',
                5 :'F',
                6 :'G',
                7 :'H',
                8 :'P',
                9 :'Q',
                10 :'R',
                11 :'S'}

    #WIP
    @classmethod
    def DFS_stack_recursive_v(self, startNode : str ,vertex_list: dict[str, list[str]], visited : dict[str : bool]):

        if (startNode in visited) and (visited.get(startNode) == True) or (startNode == 'G'):
            return
        
        visited[startNode] = True
        values = vertex_list.get(startNode)

        print(f'->{startNode}', end='')
        for neighbor in values:
            self.DFS_stack_recursive_v(neighbor, vertex_list, visited)

    @classmethod
    def DFS_stack_iterative_v(self, vertex_list: dict[str, list[str]], visited : dict[str : bool]):

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

    #WIP
    @classmethod
    def DFS_stack_recursive_adj(self, adj_matrix: np.ndarray):

        return

    @classmethod
    def DFS_stack_iterative_adj(self, start : int, adj_matrix: np.ndarray, visited : dict[str : bool]):
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


        return 0

    def isEmpty(self):
        if len(self.stack) == 0:
            return True

        return False