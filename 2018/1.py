N = int(input())
house = []
ans_lst = []
for _ in range(N):
    house.append(int(input()))
house.sort()
for i in range(N-2):
    ans_lst.append(house[i+2] - house[i])
print(min(ans_lst)/2)