N = int(input())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))


def rotater(deg):
    deg = deg % 4
    jap = [[0 for _ in range(N)] for _ in range(N)]
    if deg == 0:
        jap = table
    elif deg == 1:
        for i in range(N):
            for j in range(N):
                jap[i][j] = table[j][i]

        for i, tab in enumerate(list(reversed(jap))):
            jap[i] = list(tab)
    elif deg == 2:
        for i, tab in enumerate(list(reversed(table))):
            jap[i] = list(reversed(tab))
    elif deg == 3:
        for i in range(N):
            for j in range(N):
                jap[i][j] = table[j][i]

        for i, tab in enumerate(list(jap)):
            jap[i] = list(reversed(tab))

    return jap

horizontal_data = 0
vertical_data = 0
h_l = table[0]
v_l = []
for i in range(N):
    v_l.append(table[i][0])

h_l_s = sorted(h_l)
h_v_l = sorted(v_l)

if h_l_s == h_l:
    horizontal_data = 1
else:
    horizontal_data = 0
if h_v_l == v_l:
    vertical_data = 1
else:
    vertical_data = 0

if horizontal_data and vertical_data:
    rotater_int = 0

if not horizontal_data and vertical_data:
    rotater_int = 1

if horizontal_data and not vertical_data:
    rotater_int = 3

if not horizontal_data and not vertical_data:
    rotater_int = 2
mat = rotater(rotater_int)
for i in range(N):
    for j in range(N):
        print(mat[i][j], end=' ')
    print()