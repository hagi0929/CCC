M = int(input())  # row
N = int(input())  # column
map_matrix = []
path_lst = []
row = ''
for i in range(M):
    row = list(map(int, input().split(' ')))
    map_matrix.append(row)


def get_NM(numb):
    ans = []
    for y in range(len(map_matrix)):
        res_list = list(filter(lambda x: map_matrix[y][x] == numb, range(len(map_matrix[y]))))
        for x in res_list:
            ans.append((y, x))
    return ans


path_lst.append([(M - 1, N - 1)])
i = 0
while True:
    path_lst.append([])
    for idx in path_lst[i]:
        path_lst[i + 1] += get_NM((idx[0] + 1) * (idx[1] + 1))
    if (0, 0) in path_lst[i+1]:
        print('yes')
        break
    elif not path_lst[i]:
        print('no')
        break
    if i >= 400:
        print('no')
        break
    print(path_lst[i])
    i += 1
    path_lst[i] = list(set(path_lst[i]))