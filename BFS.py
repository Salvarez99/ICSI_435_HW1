import numpy as np
from collections import deque


class BFS:
    queue = deque()
    searchPath = [] 

    # a dictionary representing node ASCII values and pairing to index position on an array
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

    # Implementation of an iterative BFS on a vertex list
    # param_1: startNode: str
    # param_2: vertex_list: dict[str, list[str]]
    # param_3: visited: dict[str: bool]
    # return:
    @classmethod
    def BFS_queue_iterative_v(self, startNode: str, vertex_list: dict[str, list[str]], visited: dict[str: bool]):

        # Append startnode to queue
        # Change visit status to True
        self.queue.append(startNode)
        visited[startNode] = True

        while not self.isEmpty(self):

            node = self.queue.popleft()
            print(f"->{node}", end="")
            neighbors = vertex_list.get(node)

            if visited.get('G') == False or node == 'G':
                self.searchPath.append(node)

            if neighbors:
                # Iterate through neighboring nodes
                for neighbor in neighbors:
                    # If neighbor has not yet been visited
                    # Append to queue
                    # Set visit status to True
                    if visited[neighbor] == False:
                        self.queue.append(neighbor)
                        visited[neighbor] = True

        return

    # Implementation of an iterative BFS on an adjacency matrix
    # param_1: startNode: int
    # param_2: adj_matrix: np.ndarray
    # param_3: visited: dict[str: bool]
    # return:
    @classmethod
    def BFS_queue_iterative_adj(self, startNode: int, adj_matrix: np.ndarray, visited: dict[str: bool]):

        # Append startnode to queue
        self.queue.append(startNode)
        node = -1

        while not self.isEmpty(self):

            # Pop node from queue
            # Set visited status to True
            node = self.queue.popleft()
            node_key = self.vertices.get(node)
            visited[node_key] = True
            print(f"->{node_key}", end="")

            # Check if current node is goal node (6 : 'G')
            if visited.get('G') == False or node == 6:
                self.searchPath.append(node_key)


            # Iterate through columns, representing neighbors
            for col in range(len(adj_matrix)):

                node_key = self.vertices.get(col)

                # If there is an neighbor and it has not been visited
                # Change visited status to True
                # Append neighbor to queue
                if adj_matrix[node][col] == 1 and visited.get(node_key) == False:
                    visited[node_key] = True
                    self.queue.append(col)

        return

    # Implementation of a recursive DFS on a vertex list
    # param_1: startNode: str
    # param_2: vertex_list: dict[str, list[str]]
    # param_3: visited: dict[str: bool]
    # return:
    @classmethod
    def BFS_queue_recursive_v(self, startNode: str,  vertex_list: dict[str, list[str]], visited: dict[str: bool]):

        # If startnode has not been visited
        # Append it to queue
        # Change visit status to True
        # Pop startnode
        if visited.get(startNode) == False:
            self.queue.append(startNode)
            visited[startNode] = True
            startNode = self.queue.popleft()

        # If goal node has been traversed return goal node
        if startNode != 'S' and self.isEmpty(self) and visited.get('G') == True:
            print(f"->{startNode}", end="")
            return

        neighbors = vertex_list.get(startNode)
        print(f"->{startNode}", end="")

        if neighbors:
            # Iterate through neighboring nodes
            for neighbor in neighbors:
                # If neighbor has not been visited
                # Set visit status to True
                # Append to queue
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    self.queue.append(neighbor)

        # If queue is not empty
        # Recurse with next node and updated visited list
        if not self.isEmpty(self):
            nextNode = self.queue.popleft()
            self.BFS_queue_recursive_v(nextNode, vertex_list, visited)

        return

    # Implementation of a recursive DFS on an adjacency matrix
    # param_1: startNode: int
    # param_2: adj_matrix: np.ndarray
    # param_3: visited: dict[str: bool]
    # return:

    @classmethod
    def BFS_queue_recursive_adj(self, startNode: int, adj_matrix: np.ndarray, visited: dict[str: bool]):

        nodeLetter = self.vertices.get(startNode)

        # If startnode has not been visited
        # Append it to queue
        # Change visit status to True
        # Pop startnode
        if visited.get(nodeLetter) == False:
            self.queue.append(startNode)
            visited[nodeLetter] = True
            startNode = self.queue.popleft()

        # If goal node has been traversed return goal node
        if startNode != 11 and self.isEmpty(self) and visited.get('G') == True:
            print(f"->{nodeLetter}", end="")
            return

        print(f"->{nodeLetter}", end="")

        # Traverse colummns, representing neighboring nodes
        for col in range(len(adj_matrix)):

            neighborLetter = self.vertices.get(col)

            # If there is a neighbor and it has not been visited
            # Change visit status to True
            # Append neighbor to queue
            if adj_matrix[startNode][col] == 1 and visited.get(neighborLetter) == False:
                visited[neighborLetter] = True
                self.queue.append(col)

        # If queue is not empty
        # Recurse with next node and updated visited list
        if not self.isEmpty(self):
            nextNode = self.queue.popleft()
            self.BFS_queue_recursive_adj(nextNode, adj_matrix, visited)

        return

    # Helper method to check if queue is empty
    # return: boolean
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    # Helper Method to empty queue
    # return:
    @classmethod
    def empty(self):
        self.queue.clear()
        self.searchPath.clear()
