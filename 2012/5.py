R, C = map(int,input().split())
K = int(input())
cat_pos = []
boolean_map = [[1 for _ in range(C)] for _ in range(R)]


def make_map():
    maps = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(C):
        if boolean_map[0][i]:
            maps[0][i] = 1
        else:
            break
    for i in range(R):
        if boolean_map[i][0]:
            maps[i][0] = 1
        else:
            break
    for i in range(1, R):
        for j in range(1, C):
            if boolean_map[i][j]:
                maps[i][j] = maps[i-1][j] + maps[i][j-1]
            else:
                maps[0][i] = 0
    return maps

for i in range(K):
    c, r = map(int, input().split())
    cat_pos.append((c, r))
    boolean_map[c-1][r-1] = 0
final_map = make_map()
print(final_map[R-1][C-1])