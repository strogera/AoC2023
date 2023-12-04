with open("input.txt", "r") as inputFile:
    inp = inputFile.readlines()
    cards = [1 for _ in range(len(inp))]
    s = 0
    for i, line in enumerate(inp):
        gameid, rest = line.strip().split(":")
        winning, having = rest.strip().split("|")
        wh = set(map(int, winning.split())).intersection(set(map(int, having.split())))
        if len(wh) != 0:
            s += 2 ** (len(wh) - 1)
            for c in range(len(wh)):
                if i + c + 1 < len(cards):
                    cards[i + c + 1] += cards[i]
    print(s)
    print(sum(cards))
