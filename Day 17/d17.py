import heapq

class Direction:
    Up = (-1, 0)
    Down = (1, 0)
    Right = (0, 1)
    Left = (0, -1)
    Horizontal = [Left, Right]
    Vertical = [Up, Down]

def isInsideGrid(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def findPath(grid, start, end, minS, maxS):
    dist = {}
    queue = [(0, start, Direction.Right), (0, start, Direction.Down)]
    heapq.heapify(queue)
    dist[(start, Direction.Right)] = 0
    dist[(start, Direction.Down)] = 0
    visited = set()
    while queue:
        d, v, dir = heapq.heappop(queue)
        if v == end:
            return d
        if v in visited:
            continue
        visited.add((v, dir))

        newDir = Direction.Horizontal if dir == Direction.Down or dir == Direction.Up else Direction.Vertical
        for nd in newDir:
            for i in range(minS, maxS + 1):
                curPos = (v[0] + nd[0]*i, v[1] + nd[1]*i)
                if  isInsideGrid(grid, curPos):
                    alt = d + sum(grid[v[0] + nd[0]*j][v[1] + nd[1]*j] for j in range(1, i + 1))
                    if (curPos, dir) not in dist or alt < dist[(curPos, dir)]:
                        dist[(curPos, dir)] = alt
                        heapq.heappush(queue, (alt, curPos, nd))

with open("input.txt", "r") as inputFile:
    grid = [list(map(int, line.strip())) for line in inputFile.readlines()]
    print(findPath(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1), 1, 3))
    print(findPath(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1), 4, 10))