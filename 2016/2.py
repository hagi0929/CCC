Q = int(input())
N = int(input())
t1 = sorted(list(map(int, input().split())))
t2 = sorted(list(map(int, input().split())))
ans = 0
if Q == 2:
    t1 = list(reversed(t1))
for i in range(N):
    ans += t2[i] if t2[i] >= t1[i] else t1[i]
print(ans)