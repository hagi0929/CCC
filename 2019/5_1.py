import sys

sys.setrecursionlimit(5000)

N, K = map(int, input().split())
permutation = (N - K + 1) * (N - K + 2) / 2
start = K - 1
tri = [list(map(int, input().split(' '))) for _ in range(N)]
value = 0


def compute_maximum(size):
    if size == 1:
        return
    sub_size = int((2 * size + 2) / 3)
    if size == 2:
        sub_size = 1
    compute_maximum(sub_size)
    for i in range(len(tri)-size+1):
        for j in range(i+1):
            tri[i][j] = max(tri[i][j], max(tri[i + size - sub_size][j], tri[i + size - sub_size][j + size - sub_size]))


compute_maximum(K)
sum = 0
for i in range(N - K + 1):
    for j in range(i+1):
        sum += tri[i][j]
print(sum)