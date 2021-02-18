from sys import stdin

input = stdin.readline
while 1:
    n = int(input().rstrip())
    if n == 0:
        break
    coins = map(int, input().rstrip().split())
    proper_order = sorted(coins)
    
