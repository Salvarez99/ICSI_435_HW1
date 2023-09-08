import numpy as np


class DFS:

    stack: list[dict[str, list[str]]] = []

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

    @classmethod
    def DFS_stack_recursive_v(vertex_list: dict[str, list[str]]):

        return

    @classmethod
    def DFS_stack_iterative_v(self, vertex_list: dict[str, list[str]]):
        self.resetVisited(self)

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
                    if self.visited.get(i) == False:
                        self.visited[i] = True

                        nextNode = {}
                        nextNode[i] = vertex_list.get(i)

                        self.stack.append(nextNode)

        return 0

    @classmethod
    def DFS_queue_recursive_v(self, vertex_list: dict[str, list[str]]):

        return

    @classmethod
    def DFS_queue_iterative_v(self, vertex_list: dict[str, list[str]]):

        return

    @classmethod
    def DFS_stack_recursive_adj(self, adj_matrix: np.ndarray):

        return

    @classmethod
    def DFS_stack_iterative_adj(self, adj_matrix: np.ndarray):

        return

    @classmethod
    def DFS_queue_recursive_adj(self, adj_matrix: np.ndarray):

        return

    @classmethod
    def DFS_queue_iterative_adj(adj_matrix: np.ndarray):

        return

    def isEmpty(self):
        if len(self.stack) == 0:
            return True

        return False

    def resetVisited(self):
        for keys in self.visited:
            self.visited[keys] = False
        return
