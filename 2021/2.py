from sys import stdin
input = stdin.readline


def draw(VH, line):
    temp_m = matrix
    if VH:
        for i in range(N):
            temp_m[line-1][i] = 0 if temp_m[line-1][i] else 1
    else:
        for i in range(M):
            temp_m[i][line-1] = 0 if temp_m[i][line-1] else 1
    return temp_m


M = int(input())
N = int(input())
matrix = [[0 for _ in range(N)] for _ in range(M)]

K = int(input())
for i in range(K):
    RorC, num = input().rstrip().split()
    if RorC == 'R':
        camp = 1
    else:
        camp = 0
    matrix = draw(camp, int(num))
ans = 0
for i in matrix:
    ans += sum(i)
print(ans)