from sys import stdin
input = stdin.readline
J = int(input().rstrip())
A = int(input().rstrip())
size_trans = {
    'S': 0,
    'M': 1,
    'L': 2
}
shirts = {}

for i in range(J):
    s = input().rstrip()
    shirts[i+1] = size_trans[s]

ye = 0
for i in range(A):
    s, n = input().rstrip().split()
    if shirts[int(n)] >= size_trans[s]:
        ye += 1
        shirts[int(n)] = -1
print(ye)
