from queue import Queue
class Graph:
    def __init__(self,edges,direction='undirected'):
        self.direction = direction
        self.adj = self._edge2adj(edges)        
        
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

    def dfs(self,u):
        time = 0 # used with trav_time (like a global variable)
        color = {} # W (White): not visited, G (Grey): partially Visited, B (Black): visited 
        parents = {}
        trav_time = {} # [start, end]
        path = []
        # initialize nodes, parents and trav_time
        for node in self.adj:
            color[node] = 'W'
            parents[node] = None
            trav_time[node] = [-1, -1]
        path = []
        self._dfs(u,color,parents,trav_time,time,path)
        return path, parents, trav_time        

    def _dfs(self,u,color,parents,trav_time,time,path):
        color[u] = 'G'
        trav_time[u][0] = time # start time
        time += 1 # increment time once node u is visited
        path.append(u)        
        for v in self.adj[u]:
            if color[v] == 'W':
                parents[v] = u
                time = self._dfs(v,color,parents,trav_time,time,path)
        color[u] = 'B'
        trav_time[u][1] = time # end time
        time += 1
        return time

    def bfs(self,u):
        visited = {}
        level = {} # distance
        parents = {}
        output = []
        q = Queue()
        # initialize nodes, parents and level
        for node in self.adj:
            visited[node] = False
            parents[node] = None
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
                    parents[v] = u
                    level[v] = level[u] +1
                    q.put(v)
        return output, parents, level

    def distance(self,u,v):
        output, parents, level = self.bfs(u)
        path_size = level[v]
        path = []
        while v is not None:
            path.append(v)
            v = parents[v]
        return path_size, path[::-1] # reverse the path list

    def is_cyclic(self):
        # if adj is empty return False otherwise, choose a node (called first to run dfs)
        keys = list(self.adj.keys())
        if len(keys) == 0:
            return False
        else:
            first = keys[0] # get the first key in the adj list
        color = {}
        parent = {}
        # initialize the color and parents for all nodes
        for u in self.adj:
            color[u] = 'W'
            parent[u] = None
        u = first # preference to work with u instead of first
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

        for u in self.adj:
            if color[u] == 'W':
                return dfs(u,color,parent)           
        

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
    path, parents, trav_time = graph.dfs('A')
    print('path:\n', path)
    # ['A', 'B', 'F', 'M', 'G', 'I', 'D', 'J', 'H', 'N', 'E', 'C', 'L', 'K']
    
    print('parents:\n',parents)
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
    path, parents, trav_time = graph.dfs('A')
    print('path:\n', path)
    # ['A', 'B', 'F', 'M', 'D', 'I', 'G', 'J', 'H', 'C', 'L', 'K', 'E', 'N']
    
    print('parents:\n',parents)
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
    path, parents, levels = graph.bfs('A')
    print('path:\n', path)
    # ['A', 'B', 'M', 'F', 'C', 'G', 'D', 'L', 'K', 'E', 'I', 'J', 'H', 'N']

    print('parents:\n',parents)
    # {'A': None, 'B': 'A', 'M': 'A', 'F': 'B', 'C': 'B', 'L': 'C', 'K': 'C',
    #  'E': 'C', 'N': 'E', 'H': 'G', 'G': 'B', 'I': 'G', 'D': 'M', 'J': 'G'}

    print('levels:\n',levels)
    # {'A': 0, 'B': 1, 'M': 1, 'F': 2, 'C': 2, 'L': 3, 'K': 3, 'E': 3, 'N': 4,
    #  'H': 3, 'G': 2, 'I': 3, 'D': 2, 'J': 3}

    print('\nFrom A to G:')
    path_size, path = graph.distance('A','G')
    print('distance:',path_size) # 2
    print('shortest path: ',path) # ['A', 'B', 'G']

    print('\ndirected graph:')
    graph = Graph(edgeList,direction='directed')
    path, parents, levels = graph.bfs('A')
    print('path:\n', path)
    # ['A', 'B', 'M', 'F', 'C', 'G', 'D', 'L', 'K', 'E', 'I', 'J', 'H', 'N']

    print('parents:\n',parents)
    # {'A': None, 'B': 'A', 'M': 'A', 'F': 'B', 'C': 'B', 'L': 'C', 'K': 'C',
    #  'E': 'C', 'N': 'E', 'H': 'G', 'G': 'B', 'I': 'G', 'D': 'M', 'J': 'G'}

    print('levels:\n',levels)
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
    
    
