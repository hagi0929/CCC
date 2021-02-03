N = int(input())
key_lst = []
dic_lst = {}
speedLst = []
for _ in range(N):
    T, X = map(int, input().split(' '))
    key_lst.append(T)
    dic_lst[T] = X
key_lst = sorted(key_lst)
for i in range(N):
    try:
        speedLst.append(
                abs(dic_lst[key_lst[i + 1]] - dic_lst[key_lst[i]]) / abs(key_lst[i+1] - key_lst[i])
        )
    except IndexError:
        pass
print(max(speedLst))