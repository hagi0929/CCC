N = int(input())
ans = 0
for i in range(1, N-4+2):
    ang = i*(i+1)/2
    ans += ang
print(int(ans))