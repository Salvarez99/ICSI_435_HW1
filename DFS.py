import numpy as np


class DFS:

    stack: list[dict[str, list[str]]] = []

    @classmethod
    def DFS_stack_recursive_v(self, startNode : str ,vertex_list: dict[str, list[str]], visited : dict[str : bool]):
        # self.resetVisited(self)

        if (startNode in visited) and (visited.get(startNode) == True):
            return
        
        visited[startNode] = True
        values = vertex_list.get(startNode)

        print(f"->{startNode}")
        for neighbor in reversed(values):
            self.DFS_stack_recursive_v(neighbor, vertex_list,visited)







    @classmethod
    def DFS_stack_iterative_v(self, vertex_list: dict[str, list[str]], visited : dict[str : bool]):
        # self.resetVisited(self)

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
    def DFS_stack_recursive_adj(self, adj_matrix: np.ndarray):

        return

    @classmethod
    def DFS_stack_iterative_adj(self, adj_matrix: np.ndarray):

        return

    def isEmpty(self):
        if len(self.stack) == 0:
            return True

        return False


