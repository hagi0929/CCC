from sys import stdin
input = stdin.readline
N, M, D = list(map(int, input().split()))
activated = []
inactivated = []
cost_dic = {}
INF = 1000000000
# init
for i in range(M-1):
    A, B, C = list(map(int, input().split()))
    cost_dic[(A, B)] = C
    activated.append((A, B))
A, B, C = list(map(int, input().split()))
cost_dic[(A, B)] = C
inactivated.append((A, B))

print(cost_dic)