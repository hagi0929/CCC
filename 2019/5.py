import math

N, K = map(int, input().split())
permutation = (N - K + 1) * (N - K + 2) / 2
start = K - 1
tri = [list(map(int, input().split(' '))) for _ in range(N)]
value = 0
structure = [i + 1 for i in reversed(range(K))]
triangle_list = sum(tri[:K], [])  # this too
current_max = max(triangle_list)  # work on this later
ans = current_max
initial_list = list(triangle_list)
initial_max = int(current_max)

def next_items(i, j, lisst):
    back = []
    front = []
    try:
        maxmax = current_max
        for loop in range(K):
            front.append(tri[i - loop][j + structure[loop]])
            ba = tri[i - loop][j]
            back.append(ba)
            lisst.remove(ba)
        lisst += front
    except IndexError as e:
        lisst = initial_list
        maxmax = initial_max
        for loop in range(K):
            back.append(tri[i - loop][structure[loop] - 1])
            ba = tri[i - loop][structure[loop] - 1]
            lisst.remove(ba)
        front = tri[i + 1][:K]
        lisst += front

    back_max, front_max = max(back), max(front)
    if back_max > front_max:
        if maxmax > back_max:
            return maxmax, lisst
        else:
            if maxmax <= front_max:
                return front_max, lisst
            else:
                return max(triangle_list), lisst
    elif back_max <= front_max:
        if maxmax >= front_max:
            return maxmax, lisst
        else:
            return front_max, lisst

for i in range(start, N):
    for j in range(i - start + 1):
        try:
            current_max, triangle_list = next_items(i, j, triangle_list)
            ans += current_max
        except:
            print(ans)
            exit()
    initial_list = list(triangle_list)
    initial_max = int(current_max)
