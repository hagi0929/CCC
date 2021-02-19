from sys import stdin
input = stdin.readline
N = int(input())
lights = []
letters = []
dicts = {}
for i in range(N):
    rcv = input().rstrip().split()
    dicts[
        tuple(map(int, str(rcv[1])))
    ] = rcv[0]
answer = ''
word = map(int, input().rstrip())
current_direct = []
for i in word:
    current_direct.append(i)
    if tuple(current_direct) in dicts.keys():
        answer += dicts[tuple(current_direct)]
        current_direct = []
print(answer)