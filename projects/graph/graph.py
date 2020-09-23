"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = []

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if isinstance(self.vertices[v1], list):
            self.vertices[v1].append(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        queue = []
        visited = [False for x in range(len(self.vertices))]

        def bftUtil(self, vertex):

            nonlocal queue
    
            if not visited[vertex - 1]:
                print(vertex)
                queue += self.get_neighbors(vertex)
                visited[vertex - 1] = True

            if queue:
                bftUtil(self, queue.pop(0))
        
        

        bftUtil(self, starting_vertex)
    


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = []
        visited = [False for x in range(len(self.vertices))]

        stack.append(starting_vertex)

        while len(stack) > 0:

            v = stack.pop(-1)

            if not visited[v - 1]:

                visited[v - 1] = True
                print(v)
            
                for neighbor in self.get_neighbors(v):
                    stack.append(neighbor)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        stack = []
        visited = [False for x in range(len(self.vertices))]

        def dftUtil(self, vertex):

            nonlocal stack

            neighbors = self.get_neighbors(vertex)
            nextVertex = None

            if not visited[vertex - 1]:
                visited[vertex - 1] = True
                print(vertex)

            for neighbor in neighbors:
                if not visited[neighbor - 1]:
                    nextVertex = neighbor
                    break;
            
            if nextVertex:
                dftUtil(self, nextVertex)
            else:
                if stack:
                    stack.pop(-1)  
                    dftUtil(self, stack[-1])
        
        dftUtil(self, starting_vertex)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """


        queue = [[starting_vertex]]
        visited = set()

        while len(queue) > 0:

            path = queue.pop(0)

            v = path[-1]

            if v not in visited:

                visited.add(v)

                if v == destination_vertex:

                    return path
                
            
            for neighbor in self.get_neighbors(v):

                copy = path.copy()
                copy.append(neighbor)
                queue.append(copy)





    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = [[starting_vertex]]

        visited = [False for x in range(len(self.vertices))]

        while len(stack) > 0:

            path = stack.pop(-1)

            v = path[-1]

            if not visited[v - 1]:

                visited[v-1] = True 

                if v == destination_vertex:

                    return path
            
                for neighbor in self.get_neighbors(v):
                    copy = path.copy()
                    copy.append(neighbor)
                    stack.append(copy)
        

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        stack = []
        visited = [False for x in range(len(self.vertices))]
        currentPath = []
        pathList = []

        def dftUtil(self, vertex):

            nonlocal stack

            neighbors = self.get_neighbors(vertex)
            nextVertex = None
            

            if not visited[vertex - 1]:
                visited[vertex - 1] = True
                currentPath.append(vertex)

            for neighbor in neighbors:
                if not visited[neighbor - 1]:
                    nextVertex = neighbor
                    break;
            
            if nextVertex:

                if nextVertex == destination_vertex:
                    currentPath.append(nextVertex)
                    copy = currentPath.copy()
                    pathList.append(copy)

                dftUtil(self, nextVertex)
            else:
                if stack:
                    stack.pop(-1)
                    currentPath.pop(-1)
                    dftUtil(self, stack[-1])
        
        dftUtil(self, starting_vertex)

        print(min(pathList))
        return min(pathList)

    
    def deriveAdjacencyMatrix(self):

        def hasEdge(self, vertex, edge):
            if edge in self.vertices[vertex]: return 1
            else: return 0

        adjMat = [[hasEdge(self, x + 1, y + 1) for y in range(len(self.vertices))] 
                    for x in range(len(self.vertices))]

        return adjMat

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
