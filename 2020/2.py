
M = int(input())  # row
N = int(input())  # column
map_matrix = []
path_lst = []
getNM = [[] for _ in range(M * N + 1000)]
row = ''

for i in range(M):
    for j, ii in enumerate(input().split(' ')):
        getNM[int(ii)].append((i, j))

path_lst.append([(M - 1, N - 1)])
while True:
    path_lst.append([])
    for idx in path_lst[0]:
        cncn = (idx[0] + 1) * (idx[1] + 1)
        path_lst[1].extend(getNM[cncn])
        getNM[cncn] = []
    del (path_lst[0])
    if (0, 0) in path_lst[0]:
        print('yes')
        break
    elif not path_lst[0]:
        print('no')
        break

