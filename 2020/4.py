import math
N = input()
N_len = len(N)
ABC_count = {
    'A': 0,
    'B': 0,
    'C': 0,
}
for i in N:
    ABC_count[i] += 1
A_count = {
    'A': 0,
    'B': 0,
    'C': 0,
}
B_count = {
    'A': 0,
    'B': 0,
    'C': 0,
}
C_count = {
    'A': 0,
    'B': 0,
    'C': 0,
}
an = ABC_count['A']
bn = ABC_count['A'] + ABC_count['B']
cn = ABC_count['A'] + ABC_count['B'] + ABC_count['C']

for i in range(0, an):
    A_count[N[i]] += 1
for i in range(an, bn):
    B_count[N[i]] += 1
for i in range(bn, cn):
    C_count[N[i]] += 1
A_replace = A_count['B'] + A_count['C']
B_replace = B_count['A'] + B_count['C']
C_replace = C_count['A'] + C_count['B']
total = A_replace + B_replace + C_replace
total_list = [total]
c_min = total
for j in range(N_len):
    total += 0 if N[(j+an) % N_len] == 'A' else 1
    total -= 0 if N[(j)] == 'A' else 1

    total += 0 if N[(j+bn) % N_len] == 'B' else 1
    total -= 0 if N[(j+an) % N_len] == 'B' else 1

    total += 0 if N[(j+cn) % N_len] == 'C' else 1
    total -= 0 if N[(j+bn) % N_len] == 'C' else 1
    if c_min > total:
        c_min = total
print(math.ceil(c_min/2))