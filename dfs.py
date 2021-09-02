class DFS:
    global time
    def __init__(self,edges=None,direction='undirected'):
        self.adj = self._edge2adj(edges,direction)
        self.color = {} # W (White): Not visited, G (Grey): Partially visited, B (Black): visited 
        self.parents = {}
        self.trav_time = {} # [start, end]
        self.output = []
        for node in self.adj:
            self.color[node] = 'W'
            self.parents[node] = None
            self.trav_time[node] = [-1, -1]
        self.time = 0 #global
        
    def _edge2adj(self,edges,direction):
        # Converts a list of graph edeges to an adjacency list.
        # It defaults to 'undirected' graph:
        # ['A', 'B'] means 'A' --> 'B' and 'B' --> 'A'
        # Optional input 'dir' or 'directed' creates an adjacency list
        # assuming edge direction from left to right:
        # ['A', 'B'] means 'A' --> 'B'
        if edges == None:
            return {}
        else:            
            adj = {}
            for item in edges:
                if item[0] not in adj:
                    adj[item[0]] = []
                if item[1] not in adj[item[0]]:
                    adj[item[0]].append(item[1])
                if item[1] not in adj:
                    adj[item[1]] = []
                if direction == 'directed':
                    continue
                else:
                    if item[0] not in adj[item[1]]:
                        adj[item[1]].append(item[0])        
            return adj

    def dfs(self,u):          
        self.color[u] = 'G'
        self.trav_time[u][0] = self.time # start time
        self.time += 1 # increment time once node u is visited
        self.output.append(u)
        
        for v in self.adj[u]:
            if self.color[v] == 'W':
                self.parents[v] = u
                self.dfs(v)
        self.color[u] = 'B'
        self.trav_time[u][1] = self.time #end time
        self.time += 1
        return self.output

    

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
    
    dfs = DFS(edgeList)
    print(dfs.dfs('A'))
    # ['A', 'B', 'F', 'M', 'G', 'I', 'D', 'J', 'H', 'N', 'E', 'C', 'L', 'K']
    
    print(dfs.parents)
    # {'A': None, 'B': 'A', 'M': 'F', 'F': 'B',
    #  'C': 'E', 'L': 'C', 'K': 'C', 'E': 'N',
    #  'N': 'H', 'H': 'G', 'G': 'M', 'I': 'G',
    #  'D': 'I', 'J': 'G'}

    print(dfs.trav_time)
    # {'A': [0, 27], 'B': [1, 26], 'M': [3, 24], 'F': [2, 25], 'C': [14, 19],
    #  'L': [15, 16], 'K': [17, 18], 'E': [13, 20], 'N': [12, 21], 'H': [11, 22],
    #  'G': [4, 23], 'I': [5, 8], 'D': [6, 7], 'J': [9, 10]}
    
    print()

    dfs = DFS(edgeList,'directed')
    print(dfs.dfs('A'))
    # ['A', 'B', 'F', 'M', 'D', 'I', 'G', 'J', 'H', 'C', 'L', 'K', 'E', 'N']
    
    print(dfs.parents)
    # {'A': None, 'B': 'A', 'M': 'F', 'F': 'B',
    #  'C': 'B', 'L': 'C', 'K': 'C', 'E': 'C',
    #  'N': 'E', 'H': 'G', 'G': 'F', 'I': 'D',
    #  'D': 'M', 'J': 'G'}

    print(dfs.trav_time)
    # {'A': [0, 27], 'B': [1, 26], 'M': [3, 8], 'F': [2, 15], 'C': [16, 25],
    #  'L': [17, 18], 'K': [19, 20], 'E': [21, 24], 'N': [22, 23], 'H': [12, 13],
    #  'G': [9, 14], 'I': [5, 6], 'D': [4, 7], 'J': [10, 11]}
    
