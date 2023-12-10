from collections import deque


def getNeighbors(point, grid):
    neigh = set()
    cx, cy = point[0], point[1]
    match grid[cx][cy]:
        case "|":
            if grid[cx + 1][cy] != "-" and grid[cx + 1][cy] not in "7F":
                neigh.add((cx + 1, cy))
            if grid[cx - 1][cy] != "-" and grid[cx - 1][cy] not in "JL":
                neigh.add((cx - 1, cy))
        case "-":
            if grid[cx][cy + 1] != "|" and grid[cx][cy + 1] not in "FL":
                neigh.add((cx, cy + 1))
            if grid[cx][cy - 1] != "|" and grid[cx][cy - 1] not in "7J":
                neigh.add((cx, cy - 1))
        case "7":
            if grid[cx + 1][cy] != "-" and grid[cx + 1][cy] not in "F7":
                neigh.add((cx + 1, cy))
            if grid[cx][cy - 1] != "|" and grid[cx][cy - 1] not in "7J":
                neigh.add((cx, cy - 1))
        case "J":
            if grid[cx - 1][cy] != "-" and grid[cx - 1][cy] != "LJ":
                neigh.add((cx - 1, cy))
            if grid[cx][cy - 1] != "|" and grid[cx][cy - 1] != "7J":
                neigh.add((cx, cy - 1))
        case "L":
            if grid[cx - 1][cy] != "-" and grid[cx - 1][cy] != "JL":
                neigh.add((cx - 1, cy))
            if grid[cx][cy + 1] != "|" and grid[cx][cy + 1] not in "FL":
                neigh.add((cx, cy + 1))
        case "F":
            if grid[cx + 1][cy] != "-" and grid[cx + 1][cy] not in "F7":
                neigh.add((cx + 1, cy))
            if grid[cx][cy + 1] != "|" and grid[cx][cy + 1] not in "FL":
                neigh.add((cx, cy + 1))
        case "S":
            if grid[cx - 1][cy] != "-" and grid[cx - 1][cy] != "L":
                neigh.add((cx - 1, cy))
            if grid[cx + 1][cy] != "-":
                neigh.add((cx + 1, cy))
            if grid[cx][cy + 1] != "|":
                neigh.add((cx, cy + 1))
            if grid[cx][cy - 1] != "|":
                neigh.add((cx, cy - 1))

    return [(x, y) for x, y in neigh if isInRange(grid, x, y) and grid[x][y] != "."]


def isInRange(grid, x, y):
    return x in range(len(grid)) and y in range(len(grid[x]))


def bfs(startingPoint, grid):
    queue = deque()
    queue.append((*startingPoint, 0))
    visited = set()
    maxD = 0
    path = {}

    while queue:
        x1, y1, d = queue.popleft()
        v = (x1, y1)
        if v in visited:
            continue
        maxD = max(maxD, d)
        visited.add(v)
        for x, y in getNeighbors(v, grid):
            queue.append((x, y, d + 1))
            path[(x, y, grid[x][y])] = v
    return maxD


with open("input.txt", "r") as inputFile:
    grid = list(map(str.strip, inputFile.readlines()))
    startingPoint = 0
    c = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                startingPoint = (i, j)
            if grid[i][j] != ".":
                c += 1
    print(bfs(startingPoint, grid))
