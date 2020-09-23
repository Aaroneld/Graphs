
def earliest_ancestor(ancestors, starting_node):
    
    adjList = {}

    def get_neighbors(vertex_id):
            """
            Get all neighbors (edges) of a vertex.
            """
            return adjList[vertex_id]

    for ancestor in ancestors:

        if ancestor[0] not in adjList:
            adjList[ancestor[0]] = []
        
        if ancestor[1] not in adjList:
            adjList[ancestor[1]] = []
        

        adjList[ancestor[0]].append(ancestor[1])
        adjList[ancestor[1]].append(ancestor[0])


    queue = []

    queue.append([starting_node])
    visited = [False for x in range(len(adjList))]
    earliestAncestor = -1 

    while len(queue) > 0:

        path = queue.pop(0)

        v = path[-1]

        if not visited[v-1]:
            visited[v-1] = True
            if(v < earliestAncestor or len(path) > 1):
                    earliestAncestor = v
        
        

        for neighbor in get_neighbors(v):
            copy = path.copy()
            copy.append(neighbor)
            queue.append(copy)
    
    return earliestAncestor
