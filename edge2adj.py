# This function converts a list of (graph) edges to an adjacency list.
# Adjacency lists are typically used as input to DFS, BFS, etc. functions
def edge2adj(edges):
    adj = {}
    for item in edges:
        if item[0] not in adj:
            adj[item[0]] = []
        if item[1] not in adj[item[0]]:
            adj[item[0]].append(item[1])
        if item[1] not in adj:
            adj[item[1]] = []
        if item[0] not in adj[item[1]]:
            adj[item[1]].append(item[0])        
    return adj


if __name__ == "__main__":
    edgeList = [['A','B'],
                ['A','M'],
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

    print(edge2adj(edgeList))
    # {'A': ['B', 'M'], 'B': ['A', 'F', 'C', 'G'], 'M': ['A', 'F', 'G', 'D'],
    #  'F': ['B', 'M', 'G'], 'C': ['B', 'L', 'K', 'E'], 'L': ['C'], 'K': ['C'],
    #  'E': ['C', 'N', 'H'], 'N': ['E', 'H'], 'H': ['N', 'E', 'G'],
    #  'G': ['B', 'F', 'I', 'J', 'H', 'M'], 'I': ['G', 'D'], 'D': ['I', 'M'],
    #  'J': ['G']}

