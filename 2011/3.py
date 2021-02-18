from sys import stdin
input = stdin.readline

def check(mag, x, y):
    structure = [0, 1, 2, 1, 0]
    val = 0
    for i in range(mag-1, 0-1, -1):
        if not structure[(x // (5**i))] == 0:
            val += structure[(x // (5**i))] * (5**(i))
            x = x % (5**i)
        else:
            break
    if y < val:
        return True
    else:
        return False

N = int(input())
tests = []
for i in range(N):
    lst = list(map(int, input().rstrip().split()))
    tests.append("crystal" if check(lst[0], lst[1], lst[2]) else "empty")

for j in tests:
    print(j)
