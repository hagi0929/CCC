from sys import stdin
input = stdin.readline
N = int(input())
dicts = {}
for i in range(N):
    ang = input().rstrip().split()
    name = ang[0]
    r, s, d = list(map(int, ang[1:]))
    dicts[name] = (2 * r) + (3 * s) + d

Sorteds = []
prevs = -1
for i, j in sorted(dicts.items(), key=lambda x: x[1], reverse=True)[0:2]:
    Sorteds.append(i)
    if prevs == j:
        Sorteds = sorted(Sorteds)
    prevs = j

for i in Sorteds:
    print(i)