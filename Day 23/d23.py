class Node:
    def __init__(self, id, c) -> None:
        self.id = id
        self.char = c
        self.neighbors = {}

    def addNeighbor(self, node, cost = 1):
        self.neighbors[node.id] = cost

    def removeNeighbor(self, id):
        if id not in self.neighbors:
            return 0
        c = self.neighbors[id]
        del self.neighbors[id]
        return c

def getId(x, y):
    return str(x) + '.' + str(y)

def maxPath(graph):
    startingPos = getId(0, 1)
    endingPos = getId(len(grid) - 1, len(grid[-1]) - 2)
    stack = [(startingPos, 0)]
    visited = set()
    ans = 0
    while stack:
        v, cost = stack.pop()
        if cost == -1:
            visited.remove(v)
            continue
        if v == endingPos:
            ans = max(ans, cost)
            continue
        if v in visited:
            continue
        visited.add(v)
        stack.append((v, -1))
        for n in graph[v].neighbors:
            stack.append((n, cost + graph[v].neighbors[n]))

    return ans

def getGraph(grid, part1 = True):
    graph = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.' or (not part1 and grid[i][j] != '#'):
                id =  getId(i, j)
                graph[id] = Node(id, grid[i][j])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = (i + d[0], j + d[1])
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[i]):
                        if grid[nx][ny] == '.' or (not part1 and grid[nx][ny] != '#'):
                            graph[getId(nx, ny)].addNeighbor(graph[getId(i, j)])
                            graph[getId(i, j)].addNeighbor(graph[getId(nx, ny)])
                        elif grid[nx][ny] == '>':
                            nx, ny = (nx , ny + 1)
                            graph[getId(i, j)].addNeighbor(graph[getId(nx, ny)], 2)
                        elif grid[nx][ny] == 'v':
                            nx, ny = (nx + 1, ny)
                            graph[getId(i, j)].addNeighbor(graph[getId(nx, ny)], 2)
    return graph

def condense(graph):
    toDelete = []
    startingPos = (0, 1)
    endingPos = (len(grid) - 1, len(grid[-1]) - 2)
    for node in filter(lambda k: len(k.neighbors) == 2, graph.values()):
        if node.id in [getId(*startingPos), getId(*endingPos)]:
            continue
        toDelete.append(node.id)
        neId1, neId2 = node.neighbors
        c1 = graph[neId1].removeNeighbor(node.id)
        c2 = graph[neId2].removeNeighbor(node.id)
        graph[neId1].addNeighbor(graph[neId2], c1 + c2)
        graph[neId2].addNeighbor(graph[neId1], c2 + c1)
    for nId in toDelete:
        del graph[nId]
    return graph

with open("input.txt", "r") as inputFile:
    grid = inputFile.read().splitlines()
    graph = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '#':
                id =  getId(i, j)
                graph[id] = Node(id, grid[i][j])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '#':
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = (i + d[0], j + d[1])
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[i]) and grid[nx][ny] != '#':
                        graph[getId(nx, ny)].addNeighbor(graph[getId(i, j)])
                        graph[getId(i, j)].addNeighbor(graph[getId(nx, ny)])

        
    print(maxPath(getGraph(grid)))
    print(maxPath(condense(getGraph(grid, part1 = False))))