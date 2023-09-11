import numpy as np
from collections import deque


class BFS:
    queue = deque()

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
    def BFS_queue_iterative_v(self, startNode: str, vertex_list: dict[str, list[str]], visited: dict[str: bool]):

        self.queue.append(startNode)
        visited[startNode] = True

        neighbors = vertex_list.get(startNode)

        while not self.isEmpty(self):
            node = self.queue.popleft()
            print(f"->{node}", end="")
            neighbors = vertex_list.get(node)

            if node == 'G':
                return node

            if neighbors:
                for neighbor in neighbors:
                    if visited[neighbor] == False:
                        self.queue.append(neighbor)
                        visited[neighbor] = True

        return

    @classmethod
    def BFS_queue_iterative_adj(self, startNode: int, adj_matrix: np.ndarray, visited: dict[str: bool]):

        self.queue.append(startNode)
        nodeLetter = self.vertices.get(startNode)
        node = -1

        while not self.isEmpty(self):

            if node == 6:
                return node

            node = self.queue.popleft()
            nodeLetter = self.vertices.get(node)
            visited[nodeLetter] = True
            print(f"->{nodeLetter}", end="")

            for col in range(len(adj_matrix)):
                node_key = self.vertices.get(col)
                if adj_matrix[node][col] == 1 and visited.get(node_key) == False:
                    visited[node_key] = True
                    self.queue.append(col)

        return

    @classmethod
    def BFS_queue_recursive_v(self, vertex_list: dict[str, list[str]]):

        return

    @classmethod
    def BFS_queue_recursive_adj(self, adj_matrix: np.ndarray):

        return

    def isEmpty(self):
        if len(self.queue) == 0:
            return True

        return False
