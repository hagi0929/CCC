matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
boolean_matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for it in range(3):
    row = input().split()
    for jt, value in enumerate(row):
        if value == 'X':
            matrix[it][jt] = 'X'
            boolean_matrix[it][jt] = 0
        else:
            matrix[it][jt] = int(value)
            boolean_matrix[it][jt] = 1

xy_init = [['X1', 'X2', 'X3'], ['Y1', 'Y2', 'Y3']]
xy_arithmetic = [['X1', 'X2', 'X3'], ['Y1', 'Y2', 'Y3']]
vertical_ans = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
horizontal_ans = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(3):
    temp_p = []
    temp_v = []
    xy_bul = [[0, 0, 0], [0, 0, 0]]
    for j in range(3):
        temp_p.append(boolean_matrix[j][i])
        temp_v.append(matrix[j][i])
    xy_bul[1] = temp_p  # [1, 0, 0]
    xy_bul[0] = boolean_matrix[i]     # [1, 0, 1]
    xy_possible = [1 if sum(boolean_matrix[i]) >= 2 else 0, 1 if sum(temp_p) >= 2 else 0]   # [0, 1]
    xy_value = [matrix[i], temp_v]    # [[9, x, x], [16, x, 20]]
    xy_init[0][i] = matrix[i][0] if boolean_matrix[i][0] else xy_init[0][i]
    xy_init[1][i] = temp_v[0] if temp_p[0] else xy_init[1][i]
    index_lst = [[ii for ii in range(3) if xy_bul[jkjk][ii]] for jkjk in range(2)]
    value_lst = [[xy_value[jkjk][jj] for jj in range(3) if xy_bul[jkjk][jj]] for jkjk in range(2)]
    for j in range(3):
        horizontal_ans[i][j] = [value_lst[0][0], j - index_lst[0][0]] if boolean_matrix[i][j] else [matrix[j][i], 0]
        vertical_ans[j][i] = [value_lst[1][0], j - index_lst[1][0]] if boolean_matrix[j][i] else [matrix[i][j], 0]
    for index, yes_no in enumerate(xy_possible):
        if yes_no:
            slope = (value_lst[index][1]-value_lst[index][0]) / (index_lst[index][1]-index_lst[index][0])
            print(index_lst, value_lst)
            xy_init[index][i] = value_lst[index][0] - index_lst[index][0] * (value_lst[index][1]-value_lst[index][0]) / (index_lst[index][1]-index_lst[index][0])
            xy_arithmetic[index][i] = slope




    #     if not j:
    #         adder1 = xy_init[0][i]
    #         adder2 = xy_init[1][i]
    #     else:
    #         adder1 = [xy_init[0][i], (j * xy_arithmetic[0][i])]
    #         adder2 = [xy_init[1][i], (j * xy_arithmetic[1][i])]
    #     horizontal_ans[i][j] = adder1 if matrix[i][j] == 'X' else matrix[i][j]
    #     vertical_ans[j][i] = adder2 if matrix[j][i] == 'X' else matrix[j][i]
    #     try:
    #         horizontal_ans[i][j][1] = sum(horizontal_ans[i][j][1])
    #     except:
    #         pass
    #     try:
    #         vertical_ans[j][i][1] = sum(vertical_ans[j][i][1])
    #     except:
    #         pass

print('==================================')
for i in range(3):
    print(horizontal_ans[i])
print('==================================')
for i in range(3):
    print(vertical_ans[i])
