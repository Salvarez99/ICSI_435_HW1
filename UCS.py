import numpy as np
from heapq import *

class UCS: 
    priorityQueue = []

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
    def UCS_vertex_list(self, start: str, goal: str, vertexList: dict[str, list[str]], edgeList: dict[str, list[int]], visited: dict[str: bool]):

        priority_queue = []
        searchPath = []
        
        heappush(priority_queue, (0, start))
        
        while len(priority_queue) > 0:
        
            currentEdgeCost, currentNode = heappop(priority_queue)
            neighbors = vertexList.get(currentNode)
        
            if currentNode == goal:
                return
            
            if neighbors:
                for neighbor in neighbors:
                    neighborIndex = neighbors.index(neighbor)
                    neighborsEdgeCost = edgeList.get(currentNode)
                    neighborEdgeCost = neighborsEdgeCost[neighborIndex]
            
                    totalCost = currentEdgeCost + neighborEdgeCost
                    
                    #check if neighbor has been visited before OR new path is shorter
                    if visited.get(currentNode) == False:
                        if visited.get(neighbor) == False or totalCost < neighborsEdgeCost[neighborIndex]:

                            print(f"Search path cost starting from S, at {currentNode} to {neighbor}: {totalCost}\n")
                
                            neighborsEdgeCost[neighborIndex] = totalCost
                            edgeList.update({currentNode:neighborsEdgeCost})
                            heappush(priority_queue, (totalCost, neighbor))
            
            visited[currentNode] = True
        return
    

    @classmethod
    def UCS_adj_matrix(self, start: int, goal: int, adj_matrix: np.ndarray, visited: dict[str: bool]):
        
        priority_queue = []
        searchPath = []
    
        heappush(priority_queue, (0, start))
        
        while len(priority_queue) > 0:
        
            currentEdgeCost, currentNode = heappop(priority_queue)
            currentNodeLetter = self.vertices.get(currentNode)
        
            if currentNode == goal:
                return
            
            for neighbor in range(len(adj_matrix)):

                if adj_matrix[currentNode][neighbor] > 0:

                    neighborEdgeCost = adj_matrix[currentNode][neighbor]
                    totalCost = currentEdgeCost + neighborEdgeCost
                    neighborLetter = self.vertices.get(neighbor)

                    if visited.get(currentNodeLetter) == False:
                        if visited.get(neighborLetter) == False or totalCost < neighborEdgeCost:

                            print(f"Search path cost starting from S, at {currentNodeLetter} to {neighborLetter}: {totalCost}\n")

                            adj_matrix[currentNode][neighbor] = totalCost
                            heappush(priority_queue, (totalCost , neighbor))

            visited[currentNodeLetter] = True
        return
    
    def isEmpty(self):
        return len(self.priorityQueue) == 0
    
    @classmethod
    def emptyPQ(self):
        self.priorityQueue.clear()