from sys import stdin
input = stdin.readline

N = int(input())
P = []
W = []
D = []
speedlst = []
total_distance_full = 0
total_distance = 0
total_d_full = 0
total_d = 0
pwd = []
for i in range(N):
    p, w, d = list(map(int, input().rstrip().split()))
    pwd.append((p, w, d))
    total_distance_full += p * w
    total_distance += w
    total_d_full += p * w * d
    total_d += d * w + 0.000001
if total_distance == 0:
    print(0)
    exit()
middle = (total_distance_full/total_distance + total_d_full/total_d)//2
totall = 0
for p, w, d in pwd:
    jacks = abs(middle - p) - d
    totall += -(jacks * w)
totall = -(totall // (w*N))
middle += totall
middle = int(middle)
anslist = []
for i in range(-1000, 1000):
    ans = 0
    for p, w, d in pwd:
        jacks = (abs(middle+i-p)-d) if (abs(middle+i-p)-d) > 0 else 0
        ans += jacks*w
    anslist.append(ans)
print(min(anslist))