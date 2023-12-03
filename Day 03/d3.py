from math import prod


def getAdj(x, y):
    yield (x - 1, y - 1)
    yield (x, y - 1)
    yield (x - 1, y)
    yield (x + 1, y - 1)
    yield (x + 1, y + 1)
    yield (x - 1, y + 1)
    yield (x, y + 1)
    yield (x + 1, y)


with open("input.txt", "r") as inputFile:
    grid = [[]]
    for line in inputFile:
        grid.append("." + line.strip() + ".")
    grid[0] = "." * len(grid[-1])
    grid.append("." * len(grid[-1]))

    s = 0
    for x in range(1, len(grid) - 1):
        y = 1
        while y < len(grid[x]) - 1:
            if grid[x][y].isnumeric():
                for adjx, adjy in getAdj(x, y):
                    if grid[adjx][adjy] != "." and not grid[adjx][adjy].isnumeric():
                        n = grid[x][y]
                        i = y - 1
                        while i > 0 and grid[x][i].isnumeric():
                            n = grid[x][i] + n
                            i -= 1
                        i = y + 1
                        while i < len(grid[x]) and grid[x][i].isnumeric():
                            n += grid[x][i]
                            i += 1
                        s += int(n)
                        y = i - 1
                        break
            y += 1
    print(s)

    s = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "*":
                nums = []
                seen = set()
                for adjx, adjy in getAdj(x, y):
                    if grid[adjx][adjy].isnumeric() and (adjx, adjy) not in seen:
                        n = grid[adjx][adjy]
                        i = adjy - 1
                        while i > 0 and grid[adjx][i].isnumeric():
                            seen.add((adjx, i))
                            n = grid[adjx][i] + n
                            i -= 1
                        i = adjy + 1
                        while i < len(grid[adjx]) and grid[adjx][i].isnumeric():
                            seen.add((adjx, i))
                            n += grid[adjx][i]
                            i += 1
                        nums.append(int(n))
                        seen.add((adjx, adjy))
                if len(nums) == 2:
                    s += prod(nums)
    print(s)
