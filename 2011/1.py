from sys import stdin
input = stdin.readline
N = int(input().rstrip())
let = ''
for i in range(N):
    let += input().rstrip().lower()
t = let.count('t')
s = let.count('s')
if t > s:
    print('English')
elif t <= s:
    print('French')