from sys import stdin
input = stdin.readline
Tc = int(input().rstrip())
ing = []
order = []
for i in range(Tc):
    temp_ing = []
    n = int(input().rstrip())
    temp_order = [0 for _ in range(n)]
    for j in range(n):
        ii = int(input().rstrip())
        temp_ing.append(ii)
        temp_order[ii - 1] = n - (j)
    ing.append(list(reversed(temp_ing)))
    order.append(temp_order)
for i in range(len(ing)):
    print(ing[i])
    print(order[i])
for case in range(Tc):
    falling_lst = ing[case]
    middle_idx = falling_lst[-1] - 1
    prevs = 0
    display = 'Y'
    for i in order[case][: middle_idx+1]:
        if prevs <= i:
            prevs = i
            pass
        else:
            display = 'N'
            break
    if display == 'Y':
        prevs = order[case][middle_idx]
        for i in order[case][middle_idx:]:
            if prevs >= i:
                prevs = i
                pass
            else:
                display = 'N'
                break
    print(display)