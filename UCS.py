import numpy as np
from heapq import *


class UCS:

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

    # Implementation of an iterative UCS on a vertex list
    # param_1: start: str
    # param_2: goal: str
    # param_3: vertex_list: dict[str, list[str]]
    # param_4: edgeList: dict[str, list[int]]
    # param_5: visited: dict[str: bool]
    # return:
    @classmethod
    def UCS_vertex_list(self, start: str, goal: str, vertexList: dict[str, list[str]], edgeList: dict[str, list[int]], visited: dict[str: bool]):

        priority_queue = []

        # Push startnode into priority queue
        heappush(priority_queue, (0, start))

        while len(priority_queue) > 0:

            currentEdgeCost, currentNode = heappop(priority_queue)
            neighbors = vertexList.get(currentNode)

            if currentNode == goal:
                return

            if neighbors:

                # Iterate through neighboring nodes
                for neighbor in neighbors:

                    # Retreive index position of neighbor from list of neighbors
                    neighborIndex = neighbors.index(neighbor)

                    # Use currentNode to retreive edge costs of neighboring nodes
                    neighborsEdgeCosts = edgeList.get(currentNode)

                    # Use index position of neighbor to retrieve neighbors edge cost from list of neighboring edge costs
                    neighborEdgeCost = neighborsEdgeCosts[neighborIndex]

                    totalCost = currentEdgeCost + neighborEdgeCost

                    # Check if current node has been visited
                    if visited.get(currentNode) == False:
                        # Check if neighbor has been visited before OR new path is shorter
                        if visited.get(neighbor) == False or totalCost < neighborsEdgeCosts[neighborIndex]:

                            print(
                                f"Cost from S: {currentNode} -> {neighbor}: {totalCost}")


                            # Update neighbors edge cost to equate to total cost of path from S to current neighbor
                            neighborsEdgeCosts[neighborIndex] = totalCost

                            # Update edgeList dictionary entry
                            edgeList.update({currentNode: neighborsEdgeCosts})

                            # Push total cost and current neighboring node
                            heappush(priority_queue, (totalCost, neighbor))

            # Change visit status of current node to True
            visited[currentNode] = True
        return

    # Implementation of an iterative UCS on an adjacency matrix
    # param_1: start: str
    # param_2: goal: str
    # param_3: adj_matrix: np.ndarray
    # param_4: visited: dict[str: bool]
    # return:
    @classmethod
    def UCS_adj_matrix(self, start: int, goal: int, adj_matrix: np.ndarray, visited: dict[str: bool]):

        priority_queue = []

        # Push startnode into priority queue
        heappush(priority_queue, (0, start))

        while len(priority_queue) > 0:

            currentEdgeCost, currentNode = heappop(priority_queue)
            currentNodeLetter = self.vertices.get(currentNode)

            if currentNode == goal:
                return 

            # Traverse through neighboring nodes
            for neighbor in range(len(adj_matrix)):

                # If there is a neighboring node
                if adj_matrix[currentNode][neighbor] > 0:

                    # Store edge cost
                    neighborEdgeCost = adj_matrix[currentNode][neighbor]

                    totalCost = currentEdgeCost + neighborEdgeCost

                    neighborLetter = self.vertices.get(neighbor)

                    # Check if current node has been visited
                    if visited.get(currentNodeLetter) == False:
                        # Check if neighboring node has been visited OR if current path is shorter
                        if visited.get(neighborLetter) == False or totalCost < neighborEdgeCost:

                            print(
                                f"Cost from S: {currentNodeLetter} -> {neighborLetter}: {totalCost}")

                            # Update edge cost of neighboring node
                            adj_matrix[currentNode][neighbor] = totalCost

                            # Push total cost and current neighboring node
                            heappush(priority_queue, (totalCost, neighbor))

            # Change visit status of current node to True
            visited[currentNodeLetter] = True
        return
