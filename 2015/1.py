from sys import stdin
input = stdin.readline
N = int(input().rstrip())
lst = []
for _ in range(N):
    K = int(input().rstrip())
    if K == 0:
        del lst[-1]
    else:
        lst.append(K)
print(sum(lst))