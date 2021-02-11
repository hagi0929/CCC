from collections import deque
n, m = list(map(int, input().split()))
temp_map = ''
robot_position = ()
conveyor_dic = {}
answer_dic = {}
path_set = set([])
wall = []
camera = []
display = []


def set_up_conveyor(conveyor_dic):
    temp_map = map
    for i, j in conveyor_dic.items():
        y, x = i
        temp_map[y][x] = j
    return temp_map


def start_finding():
    counter = 1
    temp_wall_up_m = map
    if temp_wall_up_m[robot_position[0]][robot_position[1]] == 0:
        return
    path_deque = deque([[robot_position]])
    while 1:
        jakul = []
        for i in path_deque[0]:
            k, m = find_neighbors(i, temp_wall_up_m)
            temp_wall_up_m = m
            jakul += k
        if not jakul:
            break
        else:
            for j in jakul:
                answer_dic[j] = counter
        path_deque.append(jakul)
        path_deque.popleft()
        counter += 1


def find_neighbors(coordinate, temp_wall_up):
    i, j = coordinate
    small_ans = []
    adder = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for adder_i, adder_j in adder:
        ii, jj = i+adder_i, j+adder_j
        while 1:
            if temp_wall_up[ii][jj] < 10:
                if temp_wall_up[ii][jj]:
                    temp_wall_up[ii][jj] = 0
                    small_ans.append((ii, jj))
                break
            else:
                iii, jjj = cov(ii, jj, temp_wall_up[ii][jj])
                temp_wall_up[ii][jj] = 0
                ii, jj = iii, jjj
    return small_ans, temp_wall_up


def cov(i, j, num):
    if num == 11:
        return i, j + 1
    elif num == 12:
        return i, j - 1
    elif num == 13:
        return i - 1, j
    if num == 14:
        return i + 1, j


def set_up_wall(cameras):
    temp_map = []
    con_map = map
    for i, j in cameras:
        x = map[i]
        y = [map[iiii][j] for iiii in range(n)]
        for loop in range(j, m):
            if x[loop] == 0:
                x_i = loop
                break
        for loop in range(j, -1, -1):
            if x[loop] == 0:
                x_j = loop
                break
        for loop in range(i, n):
            if y[loop] == 0:
                y_i = loop
                break
        for loop in range(i, -1, -1):
            if y[loop] == 0:
                y_j = loop
                break
        for iii in range(x_j+1, x_i):
            temp_map.append((i,iii))
        for jjj in range(y_j+1, y_i):
            temp_map.append((jjj,j))
    for i, j in set(temp_map):
        con_map[i][j] = 0
    return con_map


for i in range(n):
    row = input()
    for j in range(m):
        if row[j] == 'S':
            robot_position = (i, j)
        elif row[j] == 'R' or row[j] == 'L' or row[j] == 'U' or row[j] == 'D':
            if row[j] == 'R':
                conveyor_dic[(i, j)] = 11
            elif row[j] == 'L':
                conveyor_dic[(i, j)] = 12
            elif row[j] == 'U':
                conveyor_dic[(i, j)] = 13
            elif row[j] == 'D':
                conveyor_dic[(i, j)] = 14
        elif row[j] == 'W':
            wall.append((i, j))
        elif row[j] == 'C':
            camera.append((i, j))
        elif row[j] == '.':
            answer_dic[(i, j)] = -1
            display.append((i, j))
    temp_map += row

temp_map = temp_map.replace('.', '1 ').replace('W', '0 ').replace('R', '11 ').replace('L', '12 ').replace('U', '13 ').\
    replace('D', '14 ').replace('C', '-1 ').replace('S', '1 ')
temp_map = list(map(int, temp_map.split()))
map = [temp_map[i*m: i*m + m] for i in range(n)]
map = set_up_wall(camera)
map = set_up_conveyor(conveyor_dic)
start_finding()
for i in sorted(display):
    print(answer_dic[i])