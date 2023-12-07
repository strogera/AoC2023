highCard = [str(c) for c in range(2, 10)] + ["T", "J", "Q", "K", "A"]
highCard2 = ["J"] + [str(c) for c in range(2, 10)] + ["T", "Q", "K", "A"]


def initialStrength(hand):
    sameCards = {c: hand.count(c) for c in hand}
    strength = 0
    if len(sameCards) == 1:
        strength = 7
    elif len(sameCards) == 2:
        if (sameCards[list(sameCards.keys())[-1]] == 4
            or sameCards[list(sameCards.keys())[-1]] == 1):
            strength = 6
        else:
            strength = 5
    elif len(sameCards) == 3:
        twopair = False
        for c in sameCards:
            if sameCards[c] == 2:
                twopair = True
                break
        if twopair:
            strength = 3
        else:
            strength = 4
    elif len(sameCards) == 4:
        strength = 2
    else:
        assert len(sameCards) == 5
        strength = 1
    return strength


def handStrength(hand):
    strength = initialStrength(hand)
    s = ""
    for c in hand:
        s += str(highCard.index(c)).zfill(2)
    return str(strength) + s


def partTwoStrength(hand):
    s = ""
    for hand2 in [hand.replace("J", c) for c in highCard2]:
        strength = initialStrength(hand2)
        s2 = ""
        for i, c in enumerate(hand2):
            s2 += str(highCard2.index(hand[i])).zfill(2)
        s = max(s, str(strength) + s2)
    return s


with open("input.txt", "r") as inputFile:
    hands = []
    for hand, bid in [l.split() for l in inputFile.readlines()]:
        hands.append((hand, int(bid)))

    print(sum( (i + 1) * h[1] for i, h in enumerate(sorted(hands, key=lambda h: handStrength(h[0])))))
    print(sum( (i + 1) * h[1] for i, h in enumerate(sorted(hands, key=lambda h: partTwoStrength(h[0])))))
