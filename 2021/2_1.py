from sys import stdin
input = stdin.readline

M = int(input())
N = int(input())

K = int(input())
vertical = dict.fromkeys(range(N), 0)
horizontal = dict.fromkeys(range(M), 0)
for i in range(K):
    RorC, num = input().rstrip().split()
    if RorC == 'R':
        horizontal[int(num)-1] += 1
    else:
        vertical[int(num)-1] += 1
count_h = 0
for i in horizontal.values():
    count_h += 1 if i % 2 else 0

count_v = 0
for i in vertical.values():
    count_v += 1 if i % 2 else 0

alternative_h = M - count_h
alternative_v = N - count_v

print(count_h*alternative_v + alternative_h*count_v)