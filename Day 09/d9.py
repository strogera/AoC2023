with open("input.txt", "r") as inputFile:
    data = [[int(x) for x in line.strip().split()] for line in inputFile.readlines()]
    s = 0
    s2 = 0
    for line in data:
        seq = [line]
        while any([x != 0 for x in seq[-1]]):
            seq.append([])
            for i in range(len(seq[-2]) - 1):
                seq[-1].append(seq[-2][i + 1] - seq[-2][i] )
        s += sum(l[-1] for l in seq)
        c = 0
        for i in range(len(seq) -2, -1, -1):
            c = seq[i][0] - c
        s2 += c

    print(s)
    print(s2)
