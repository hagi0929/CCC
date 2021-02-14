from sys import stdin
input = stdin.readline
N, M = list(map(int, input().split()))
pho = list(map(int, input().split()))
EdgeList = []
dic = {}
no_repetition = [True for _ in range(N)]


def make_map(start_no):
    Address = [[start_no]]
    VisitedVertex = []
    stack = [start_no]
    idx = 0
    path = []
    Address = dict.fromkeys(list(range(N)), [])
    Address[start_no] = [start_no]
    while stack:
        current = stack.pop()
        for neighbor in dic[current]:
            prev_A = list(Address[idx])
            if not neighbor in VisitedVertex:
                Address[neighbor] = Address[current] + [neighbor]
                prev_A.append(neighbor)
                stack.append(neighbor)
        VisitedVertex.append(current)
        idx = VisitedVertex.index(current) + 1
    return VisitedVertex, Address

    # pho_left = dict.fromkeys(pho, 1)
    # time_dic = {0: [start_no]}
    # time = 0
    # current_lst = [start_no]
    # while any(pho_left.values()):
    #     time += 1
    #     for current in current_lst:
    #         no_repetition[current] = False
    #         time_dic[time] = []
    #         current_lst = []
    #         for i in dic[current]:
    #             if no_repetition[i]:
    #                 time_dic[time].append(i)
    #                 current_lst.append(i)
    #                 if pho_left:
    #                     pho_left[i] = False
    #
    #             print(time_dic)


for i in range(N-1):
    address = []
    d1, d2 = list(map(int, input().split()))
    EdgeList.append((d1, d2))
    if d1 in dic.keys():
        dic[d1].append(d2)
    else:
        dic[d1] = [d2]

    if d2 in dic.keys():
        dic[d2].append(d1)
    else:
        dic[d2] = [d1]
print(make_map(0))
print(dic)