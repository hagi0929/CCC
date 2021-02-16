from sys import stdin
input = stdin.readline
N = int(input().rstrip())
lst = []
dic = {

}
check = []
for i in range(N):
    num = int(input().rstrip())
    lst.append(num)
    if num in dic.keys():
        dic[num] += 1
    else:
        dic[num] = 1
soted = sorted(dic.values(), reverse=True)
d_max = []
find = (soted[0], soted[1]) if len(soted) >= 2 else (soted[0], soted[0])
finded = [[], []]
for k, v in dic.items():
    for amp, i in enumerate(find):
        if v == i:
            finded[amp].append(k)
final = []
final.append(max(finded[0]) - min(finded[1]))
final.append(max(finded[1]) - min(finded[0]))
print(max(final))