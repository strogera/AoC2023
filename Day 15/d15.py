from collections import defaultdict


def hashS(s):
    h = 0
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h


with open("input.txt", "r") as inputFile:
    hashSeq = inputFile.read().strip().split(",")

    boxes = defaultdict(list)

    part1 = 0
    for s in hashSeq:
        part1 += hashS(s)
        t = s.split("-")[0].split("=")[0]
        box = boxes[hashS(t)]
        temp = [a for a, b in box]
        p = temp.index(t) if t in temp else -1
        if "-" in s:
            if p != -1:
                box.pop(p)
        elif "=" in s:
            if p != -1:
                box[p][1] = int(s[-1])
            else:
                box.append([s[:-2], int(s[-1])])
    part2 = sum(sum((i + 1) * (si + 1) * l[1] for si, l in enumerate(box)) for i, box in boxes.items())

    print(part1)
    print(part2)
