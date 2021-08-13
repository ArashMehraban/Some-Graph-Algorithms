def edge2adj(edges,direction='undirected'):
    # Converts a list of graph edeges to an adjacency list.
    # It defaults to 'undirected' graph:
    # ['A', 'B'] means 'A' --> 'B' and 'B' --> 'A'
    # Optional input 'dir' or 'directed' creates an adjacency list
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
        if direction == 'dir' or direction == 'directed':
            continue
        else:
            if item[0] not in adj[item[1]]:
                adj[item[1]].append(item[0])        
    return adj


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

    print('Undirected:')
    print(edge2adj(edgeList))
    # {'A': ['B', 'M'], 'B': ['A', 'F', 'C', 'G'], 'M': ['A', 'F', 'G', 'D'],
    #  'F': ['B', 'M', 'G'], 'C': ['B', 'L', 'K', 'E'], 'L': ['C'], 'K': ['C'],
    #  'E': ['C', 'N', 'H'], 'N': ['E', 'H'], 'H': ['N', 'E', 'G'],
    #  'G': ['B', 'F', 'I', 'J', 'H', 'M'], 'I': ['G', 'D'], 'D': ['I', 'M'],
    #  'J': ['G']}
  
    directedEdgeList = [['A','B'],
                        ['A','C'],
                        ['A','D'],
                        ['D','E'],
                        ['F','E'],
                        ['G','F'],
                        ['G','A'],
                        ['C','D']]

    print('\nDirected:')
    print(edge2adj(directedEdgeList, 'directed'))
    # {'A': ['B', 'C', 'D'], 'B': [], 'C': ['D'], 'D': ['E'], 'E': [], 'F': ['E'],
    # 'G': ['F', 'A']}

