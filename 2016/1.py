from builtins import dict

N1 = list(input())
ss = input()
len_N2 = len(set(ss.replace('*', '')))
N2 = list(ss)
dic1 = dict.fromkeys(list(set(N1 + N2)), 0)
dic2 = dict.fromkeys(list(set(N1 + N2)), 0)

for i, j in zip(N1, N2):
    dic1[i] += 1
    dic2[j] += 1
star_diff = 0
if '*' in N2:
    star_diff = dic2['*']
val = 0
if sorted(dic1.keys()) == sorted(dic2.keys()) or abs(len_N2-len(set(N1))) >= star_diff:
    for i, j in zip(sorted(dic1.items()), sorted(dic2.items())):
        if i[1] < j[1]:
            val += j[1] - i[1]
    if star_diff >= val:
        print('A')
    else:
        print('N')
