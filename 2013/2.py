from sys import stdin
input = stdin.readline
W = int(input().rstrip())
N = int(input().rstrip())
weightList = []
for _ in range(N):
    c = int(input().rstrip())
    weightList.append(c)

for i in range(N):
    start = i - 3 if i >= 4 else 0
    if sum(weightList[start: i+1]) > W:
        print(i)
        exit()
print(N)