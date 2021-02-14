from sys import stdin
input = stdin.readline
G = int(input())
P = int(input())
plane = []

for i in range(P):
    plane.append(int(input()))


def find(port):
    if port == dic[port]:
        return dic[port]
    temp = find(dic[port])
    dic[port] = temp
    return dic[port]


def swap(port, idk_name):
    t1 = find(port)
    t2 = find(idk_name)
    dic[t1] = t2


dic = {i: i for i in range(G + 1)}
count = 0
for i in plane:
    x = find(i)
    if x == 0:
        break
    swap(x, x-1)
    count += 1
print(count)