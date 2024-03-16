
class Direction:
    Up = (-1, 0)
    Down = (1, 0)
    Right = (0, 1)
    Left = (0, -1)
    Horizontal = [Left, Right]
    Vertical = [Up, Down]

def getCurArea(x, y, direction, length):
    dy, dx = direction[0]*length, direction[1]*length
    x, y = x + dx, y + dy
    return x, y, x*dy

with open("input.txt", "r") as inputFile:
    pos = (0, 0)
    toDir = {'U' : Direction.Up , 'D' : Direction.Down, 'L' : Direction.Left , 'R' : Direction.Right}
    toDirPart2 = {'0': Direction.Right, '1': Direction.Down, '2': Direction.Left, '3': Direction.Up}
    grid = {pos}
    x, y = 0, 0
    x2, y2 = 0, 0
    area, area2 = 0, 0
    p, p2 = 0, 0
    for line in inputFile.readlines():
        d, l, c, = line.strip().split(' ')
        d2, l2 = toDirPart2[c[-2]], int(c[2:-2], 16)
        d, l = toDir[d], int(l)

        p += l
        p2 += l2

        x, y, narea = getCurArea(x, y, d, l)
        x2, y2, narea2 = getCurArea(x2, y2, d2, l2)
        area += narea
        area2 += narea2
    print(area + p//2 + 1)
    print(area2 + p2//2 + 1)