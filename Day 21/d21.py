def formula(n, a, b, c):
    return a + n * (b - a + (n - 1) * (c - 2*b + a) // 2)

def bfs(graph, start, limit):
    prevRing = set()
    curRing = set()
    prevRing.add(start)
    part2 = []
    for i in range(1, len(grid)*3 + 1):
        for c in prevRing:
            for v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newNeigh = (c[0] + v[0], c[1] + v[1])
                newNeighInG = ((c[0] + v[0])%131, (c[1] + v[1])%131)
                if graph[newNeighInG[0]][newNeighInG[1]] == '.':
                    curRing.add(newNeigh)
        if i == 64:
            print(len(curRing)) #part1 
        if i % len(grid) == 65:
            part2.append(len(curRing))
        prevRing = curRing
        curRing = set()
    print(formula(26501365 // 131, *part2)) #part2



with open("input.txt", "r") as inputFile:
    grid = [line.strip() for line in inputFile.readlines()]
    startingPos = None
    for i, _ in enumerate(grid):
        if startingPos:
            break
        for j, _ in enumerate(grid[i]):
            if grid[i][j] == 'S':
                startingPos = (i, j)
                break
    grid[startingPos[0]] = grid[startingPos[0]].replace('S', '.')
    assert(startingPos)
    bfs(grid, startingPos, 64)