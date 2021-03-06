from queue import Queue
class Graph:
    def __init__(self,edges,direction='undirected'):
        self.direction = direction
        self.adj = self._edge2adj(edges)
        self.nodes = list(self.adj.keys())
        self.edges = self._edgeWeights(edges)
        
    def _edge2adj(self,edges):
        # Converts a list of Graph edeges to an adjacency list.
        # It defaults to 'undirected' graph:
        # ['A', 'B'] means 'A' --> 'B' and 'B' --> 'A'
        # Optional input 'directed': creates an adjacency list
        # assuming edge direction from left to right:
        # ['A', 'B'] means 'A' --> 'B'                  
        adj = {}
        for item in edges:
            if item[0] not in adj:
                adj[item[0]] = []
            if item[1] not in adj[item[0]]:
                adj[item[0]].append(item[1])
            if item[1] not in adj:
                adj[item[1]] = []
            if self.direction == 'directed':
                continue
            else:
                if item[0] not in adj[item[1]]:
                    adj[item[1]].append(item[0])        
        return adj

    def _edgeWeights(self,edges):
        # Creates a dictionary of edges-->weight
        # Note: use tuples since list is unhashable
        # ['A','B', W] converts to {('A','B') : W}
        # ['A','B'] converts to {('A','B') : 1} 
        col_sz = len(edges[0])
        edgesMap = {}
        for item in edges:
            if col_sz == 2:
                W = 1
            if col_sz == 3:
                W = item[2]
            edgesMap[(item[0],item[1])] = W
        return edgesMap           

    def dfs(self,u):
        time = 0 # used statically (passed to AND returned from the recursive function _dfs)
        color = {} # W (White): not visited, G (Grey): partially visited, B (Black): fully visited 
        parent = {}
        trav_time = {} # [start, end]
        path = []
        # initialize nodes, parent and trav_time
        for node in self.adj:
            color[node] = 'W'
            parent[node] = None
            trav_time[node] = [-1, -1]
        path = []
        self._dfs(u,color,parent,trav_time,time,path)
        return path, parent, trav_time        

    def _dfs(self,u,color,parent,trav_time,time,path):
        color[u] = 'G'
        trav_time[u][0] = time # start time
        time += 1 # increment time once node u is visited
        path.append(u)        
        for v in self.adj[u]:
            if color[v] == 'W':
                parent[v] = u
                time = self._dfs(v,color,parent,trav_time,time,path)
        color[u] = 'B'
        trav_time[u][1] = time # end time
        time += 1
        return time

    def bfs(self,u):
        visited = {}
        level = {} # distance
        parent = {}
        output = []
        q = Queue()
        # initialize nodes, parent and level
        for node in self.adj:
            visited[node] = False
            parent[node] = None
            level[node] = -1
            
        # set values for the given Node: u
        visited[u] = True
        level[u] = 0
        q.put(u)
        #bfs
        while not q.empty():
            u = q.get() # pop the queue
            output.append(u)
            # explore all adjacent nodes of u
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    level[v] = level[u] +1
                    q.put(v)
        return output, parent, level

    def distance(self,u,v):
        output, parent, level = self.bfs(u)
        path_size = level[v]
        path = []
        while v is not None:
            path.append(v)
            v = parent[v]
        return path_size, path[::-1] # reverse the path list

    def is_cyclic(self):
        if len(self.nodes) == 0: 
            return False
        color = {}
        parent = {}
        # initialize color and parent for all nodes
        for u in self.adj:
            color[u] = 'W'
            parent[u] = None

        u = self.nodes[0] # choose a node (first one in this case to run dfs with)
        def dfs(u,color,parent):
            color[u] = 'G'
            for v in self.adj[u]:
                if color[v] == 'W':
                    if self.direction == 'undirected':
                        parent[v] = u
                    if dfs(v,color,parent):
                        return True
                elif self.direction == 'directed' and color[v] == 'G':
                    return True
                elif self.direction == 'undirected' and color[v] == 'G' and parent[u] != v:
                    return True
            color[u] = 'B'
            return False

        cyc = False
        for u in self.adj:
            if color[u] == 'W':
                cyc = dfs(u,color,parent)
                if cyc:
                    break
        return cyc

    def articulation(self):
        # Based on Tarjan's algorithm
        # initialize discovery time (disc), lowest possible discovery time (low),
        # parent and articulation points (AP)
        disc = {}
        low = {}
        parent = {}
        AP = {}
        for node in self.nodes:
            disc[node] = -1
            low[node] = -1
            parent[node] = None
            AP[node] = False

        time = 0 # used statically (passed to AND returned from the recursive function _articulation_dfs)

        for node in self.nodes:
            if disc[node] == -1:
                time = self._articulation_dfs(node, disc,low, parent, AP, time)

        articulation_points = []
        for ap in AP:
            if AP[ap] == True:
                articulation_points.append(ap)
        return articulation_points

        
    def _articulation_dfs(self,u, disc,low, parent, AP, time):
        disc[u] = time
        low[u] = time
        time += 1
        children = 0

        for v in self.adj[u]:
            if disc[v] == -1: # if v is not visited
                children += 1
                parent[v] = u
                time = self._articulation_dfs(v, disc,low, parent, AP, time)
                low[u] = min(low[u], low[v])
                # if u is root
                if parent[u] == None and children > 1:
                    AP[u] = True
                # if a component separable
                if parent[u] != None and low[v] >= disc[v]:
                    AP[u] = True
            elif v != parent[u]: # Ignore child to parent edge
                low[u] = min(low[u],disc[v])
        return time
        
        
if __name__ == "__main__":
    edgeList = [['A','B'],
                ['A','M'],
                ['B','F'],
                ['F','M'],
                ['B','C'],
                ['C','L'],
                ['C','K'],
                ['C','E'],
                ['E','N'],
                ['N','H'],
                ['E','H'],
                ['B','G'],
                ['F','G'],
                ['G','I'],
                ['D','I'],
                ['G','J'],
                ['G','H'],
                ['G','M'],
                ['M','D']]

    print('\nTest DFS:\n')
    print('undirected graph:')
    graph = Graph(edgeList)
    path, parent, trav_time = graph.dfs('A')
    print('path:\n', path)
    # ['A', 'B', 'F', 'M', 'G', 'I', 'D', 'J', 'H', 'N', 'E', 'C', 'L', 'K']
    
    print('parent:\n',parent)
    # {'A': None, 'B': 'A', 'M': 'F', 'F': 'B',
    #  'C': 'E', 'L': 'C', 'K': 'C', 'E': 'N',
    #  'N': 'H', 'H': 'G', 'G': 'M', 'I': 'G',
    #  'D': 'I', 'J': 'G'}

    print('trav_time:\n',trav_time)
    # {'A': [0, 27], 'B': [1, 26], 'M': [3, 24], 'F': [2, 25], 'C': [14, 19],
    #  'L': [15, 16], 'K': [17, 18], 'E': [13, 20], 'N': [12, 21], 'H': [11, 22],
    #  'G': [4, 23], 'I': [5, 8], 'D': [6, 7], 'J': [9, 10]}
    
    print('\ndirected graph:')

    graph = Graph(edgeList,direction='directed')
    path, parent, trav_time = graph.dfs('A')
    print('path:\n', path)
    # ['A', 'B', 'F', 'M', 'D', 'I', 'G', 'J', 'H', 'C', 'L', 'K', 'E', 'N']
    
    print('parent:\n',parent)
    # {'A': None, 'B': 'A', 'M': 'F', 'F': 'B',
    #  'C': 'B', 'L': 'C', 'K': 'C', 'E': 'C',
    #  'N': 'E', 'H': 'G', 'G': 'F', 'I': 'D',
    #  'D': 'M', 'J': 'G'}

    print('trav_time:\n',trav_time)
    # {'A': [0, 27], 'B': [1, 26], 'M': [3, 8], 'F': [2, 15], 'C': [16, 25],
    #  'L': [17, 18], 'K': [19, 20], 'E': [21, 24], 'N': [22, 23], 'H': [12, 13],
    #  'G': [9, 14], 'I': [5, 6], 'D': [4, 7], 'J': [10, 11]}

    print('\n--------------------------------------\n')
    print('Test BFS:\n')
    print('undirected graph:')
    graph = Graph(edgeList)
    path, parent, level = graph.bfs('A')
    print('path:\n', path)
    # ['A', 'B', 'M', 'F', 'C', 'G', 'D', 'L', 'K', 'E', 'I', 'J', 'H', 'N']

    print('parent:\n',parent)
    # {'A': None, 'B': 'A', 'M': 'A', 'F': 'B', 'C': 'B', 'L': 'C', 'K': 'C',
    #  'E': 'C', 'N': 'E', 'H': 'G', 'G': 'B', 'I': 'G', 'D': 'M', 'J': 'G'}

    print('level:\n',level)
    # {'A': 0, 'B': 1, 'M': 1, 'F': 2, 'C': 2, 'L': 3, 'K': 3, 'E': 3, 'N': 4,
    #  'H': 3, 'G': 2, 'I': 3, 'D': 2, 'J': 3}

    print('\nFrom A to G:')
    path_size, path = graph.distance('A','G')
    print('distance:',path_size) # 2
    print('shortest path: ',path) # ['A', 'B', 'G']

    print('\ndirected graph:')
    graph = Graph(edgeList,direction='directed')
    path, parent, level = graph.bfs('A')
    print('path:\n', path)
    # ['A', 'B', 'M', 'F', 'C', 'G', 'D', 'L', 'K', 'E', 'I', 'J', 'H', 'N']

    print('parent:\n',parent)
    # {'A': None, 'B': 'A', 'M': 'A', 'F': 'B', 'C': 'B', 'L': 'C', 'K': 'C',
    #  'E': 'C', 'N': 'E', 'H': 'G', 'G': 'B', 'I': 'G', 'D': 'M', 'J': 'G'}

    print('level:\n',level)
    # {'A': 0, 'B': 1, 'M': 1, 'F': 2, 'C': 2, 'L': 3, 'K': 3, 'E': 3, 'N': 4,
    #  'H': 3, 'G': 2, 'I': 3, 'D': 2, 'J': 3}

    print('\nFrom A to G:')
    path_size, path = graph.distance('A','G')
    print('distance:',path_size)  # 2
    print('shortest path: ',path) # ['A', 'B', 'G']

    print('\n--------------------------------------\n')
    print('Different test cases:\n')
    edgeList = [['A','C'],
                ['A','B'],
                ['B','D'],
                ['D','A'],
                ['D','E']]
    g = Graph(edgeList,direction='directed')
    print('\nCyclye in directed graph:')
    print(g.is_cyclic()) #True

    edgeList = [['A','C'],
                ['A','B'],
                ['A','D'],
                ['B','D'],
                ['D','E']]
    g = Graph(edgeList)
    print('\nCyclye in undirected graph:')
    print(g.is_cyclic()) #True

    print('\n--------------------------------------\n')
    print('Test Articulation Points:')
    edgeList = [['A','B'],
                ['A','C'],
                ['A','D'],
                ['D','E'],
                ['D','F']]
    g = Graph(edgeList)
    print(g.articulation()) #['A', 'D'] 
    
    
