from sys import stdin
input = stdin.readline
Tc = int(input().rstrip())
ing = []
order = []
idx = []
for i in range(Tc):
    temp_ing = []
    n = int(input().rstrip())
    idx.append(n)
    for j in range(n):
        ii = int(input().rstrip())
        temp_ing.append(ii)
    ing.append(temp_ing)
answer_lst = []
for case in range(Tc):
    branch = []
    what_we_need = 1
    recent_branch = 0
    lake = []
    while 1:
        try:
            i = ing[case].pop()
        except IndexError:
            while 1:
                recent_branch = branch.pop() if branch else None
                if what_we_need == recent_branch:
                    lake.append(what_we_need)
                    what_we_need += 1
                else:
                    branch.append(i)
                    recent_branch = branch[-1]
                    break
            break
        if what_we_need == i:
            lake.append(what_we_need)
            what_we_need += 1
        else:
            while 1:
                if what_we_need == recent_branch:
                    lake.append(branch.pop()if branch else what_we_need)
                    what_we_need += 1
                    recent_branch = branch[-1]
                else:
                    branch.append(i)
                    recent_branch = branch[-1]
                    break
    if len(lake) == idx[case]:
        print('Y')
    else:
        print('N')


    # falling_lst = ing[case]
    # middle_idx = falling_lst[-1] - 1
    # prevs = 0
    # display = 'Y'
    # for i in order[case][: middle_idx+1]:
    #     if prevs <= i:
    #         prevs = i
    #         pass
    #     else:
    #         display = 'N'
    #         break
    # if display == 'Y':
    #     prevs = order[case][middle_idx]
    #     for i in order[case][middle_idx:]:
    #         if prevs >= i:
    #             prevs = i
    #             pass
    #         else:
    #             display = 'N'
    #             break
    # print(display)