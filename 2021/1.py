N = int(input())
side = list(map(int, input().split()))
bottom = list(map(int, input().split()))
arealst = []
for i in range(N):
    arealst.append(((side[i] + side[i+1])/2)*bottom[i])
print(sum(arealst))