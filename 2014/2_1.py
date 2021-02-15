N = int(input())
f = input().split()
s = input().split()
if all([i == j for i, j in zip(f, reversed(s))]):
    print('good')
else:
    print('bad')
