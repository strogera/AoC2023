#from: https://topaz.github.io/paste/#XQAAAQAvAQAAAAAAAAA0m0pnuFI8c82uPD0wiI6r5tRTRja96TZwDRjCPYGCOqExbvZ5+0jns153Ad69VqBjBqQaUspo7NrNRpDc/+ZGFdNSun/wnVOT1qXxnAamzkwKLhxHiCZtWhGd8B/ZVlpxob4CxZmqu+ni/or+caAnmcMG4xTqEH9UT10sSC20Jtq3yetoZEkBm6TqysbKJlV/9noYXwMQIZPn9RpkyjgtIf4yVG1f/rH45+y+/ZBb3VCSDZhg7WGjPNptygpe3fRdyDtq8WnADgtT5icHWOo5yexJky3ebI/tBCnO7+3k4rLE6hL9Eg7kkfrsksYD/3WZAgA=

from collections import defaultdict

G = defaultdict(set)

for line in open('input.txt'):
    u, *vs = line.replace(':','').split()
    for v in vs:
        G[u].add(v)
        G[v].add(u)

S = set(G)

count = lambda v: len(G[v]-S)

while sum(map(count, S)) != 3:
    S.remove(max(S, key=count))

print(len(S) * len(set(G)-S))
