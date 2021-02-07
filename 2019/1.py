N = input()
num = {
    'H': 0,
    'V': 0
}
list = [
    [1, 2],
    [3, 4]
]


def H():
    temp = list[0]
    list[0] = list[1]
    list[1] = temp


def V():
    temp = list[0][0]
    list[0][0] = list[0][1]
    list[0][1] = temp
    temp = list[1][0]
    list[1][0] = list[1][1]
    list[1][1] = temp


for i in N:
    num[i] += 1
for i, j in num.items():
    num[i] = j % 2
if num['V'] == 1:
    V()
if num['H'] == 1:
    H()

print(f'{list[0][0]} {list[0][1]}\n{list[1][0]} {list[1][1]}')
