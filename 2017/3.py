from itertools import combinations
from collections import Counter

def endnow(rep):
    print(rep_dic[rep[0]]//2,1)
    exit()
N = int(input())
plate = list(map(int, input().split()))
no_rep = list(set(plate))
rep_dic = dict.fromkeys(no_rep, 0)
ans_dic = {}
for j in plate:
    rep_dic[j] += 1
comb = combinations(no_rep, 2) if len(no_rep) >= 2 else endnow(no_rep)
for i, j in comb:
    if i + j in ans_dic:
        ans_dic[i + j] += min(rep_dic[i], rep_dic[j])
    else:
        ans_dic[i + j] = min(rep_dic[i], rep_dic[j])
for i in no_rep:
    un = i*2
    if un in ans_dic:
        ans_dic[un] += rep_dic[i]//2
    else:
        ans_dic[un] = rep_dic[i]//2
val = ans_dic.values()
maxs = max(val)
print(maxs, Counter(val)[maxs])