from sys import stdin
from itertools import combinations, product

possible_comb = list(combinations([1, 2, 3, 4], 2))
score = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
}
possible_score = [(3, 0), (0, 3), (1, 1)]
input = stdin.readline
T = int(input().rstrip())
G = int(input().rstrip())
game_board = []

for i in range(G):
    A, B, A_s, B_s = list(map(int, input().rstrip().split()))
    if A_s > B_s:
        score[A] += 3
    elif A_s < B_s:
        score[B] += 3
    elif A_s == B_s:
        score[A] += 1
        score[B] += 1
    possible_comb.remove(tuple(sorted((A, B))))
left_N = len(possible_comb)
run_on = []

pogi = product(possible_score, repeat=left_N)
final_score = []
for i in pogi:
    temp_score = dict(score)
    for comb, left in zip(i, possible_comb):
        temp_score[left[0]] += comb[0]
        temp_score[left[1]] += comb[1]
    final_score.append(temp_score)
print(final_score)
counter = 0
for i in final_score:
    sorting = sorted(i.values(), reverse=True)
    if sorting[0] == sorting[1]:
        print('kon')
        pass
    elif i[3] == sorting[0]:
        counter += 1
print(counter)
