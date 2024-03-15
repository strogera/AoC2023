from collections import defaultdict


class Direction:
    Up = (-1, 0)
    Down = (1, 0)
    Right = (0, 1)
    Left = (0, -1)
    Horizontal = [Left, Right]
    Vertical = [Up, Down]


def isInsideGrid(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def newPos(pos, direction):
    return ((pos[0] + direction[0], pos[1] + direction[1]), direction)


cache = defaultdict(int)


def bfs(pos, direction):

    if (pos, direction) in cache:
        return cache[(pos, direction)]

    canCache = True
    cacheDistance = defaultdict(int)
    visited = set()
    timesVisited = defaultdict(set)
    q = [(pos, direction)]
    i = 0

    while q:
        i += 1
        pos, direction = q.pop(0)
        if not isInsideGrid(grid, pos) or (
            pos in visited and direction in timesVisited[pos]
        ):
            continue
        visited.add(pos)
        timesVisited[pos].add(direction)
        if direction in Direction.Horizontal and grid[pos[0]][pos[1]] == "|":
            canCache = False
        elif direction in Direction.Vertical and grid[pos[0]][pos[1]] == "-":
            canCache = False
        if canCache:
            cacheDistance[(pos, direction)] = i - 1

        match grid[pos[0]][pos[1]]:
            case ".":
                q.append(newPos(pos, direction))
            case "-":
                if direction in Direction.Horizontal:
                    q.append(newPos(pos, direction))
                else:
                    q.append(newPos(pos, Direction.Right))
                    q.append(newPos(pos, Direction.Left))
            case "|":
                if direction in Direction.Vertical:
                    q.append(newPos(pos, direction))
                else:
                    q.append(newPos(pos, Direction.Up))
                    q.append(newPos(pos, Direction.Down))
            case "/":
                if direction == Direction.Down:
                    q.append(newPos(pos, Direction.Left))
                elif direction == Direction.Up:
                    q.append(newPos(pos, Direction.Right))
                elif direction == Direction.Right:
                    q.append(newPos(pos, Direction.Up))
                else:
                    q.append(newPos(pos, Direction.Down))
            case "\\":
                if direction == Direction.Down:
                    q.append(newPos(pos, Direction.Right))
                elif direction == Direction.Up:
                    q.append(newPos(pos, Direction.Left))
                elif direction == Direction.Right:
                    q.append(newPos(pos, Direction.Down))
                else:
                    q.append(newPos(pos, Direction.Up))

    for (k, d), v in cacheDistance.items():
        cache[(k, d)] = max(cache[(k, d)], len(visited) - v)
    return len(visited)


with open("input.txt", "r") as inputFile:
    grid = [line.strip() for line in inputFile.readlines()]
    part2 = 0
    for i in range(len(grid)):
        part2 = max(part2, bfs((0, i), Direction.Down))
        part2 = max(part2, bfs((len(grid) - 1, i), Direction.Up))
        part2 = max(part2, bfs((i, 0), Direction.Right))
        part2 = max(part2, bfs((len(grid) - 1, i), Direction.Left))
    print(bfs((0, 0), Direction.Right))
    print(part2)
