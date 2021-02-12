N = int(input())
T1 = list(map(int, input().split()))
T2 = list(map(int, input().split()))
ans = 0
T1_ans = 0
T2_ans = 0
for i in range(N):
    T1_ans += T1[i]
    T2_ans += T2[i]
    if T1_ans == T2_ans:
        ans = i + 1
print(ans)