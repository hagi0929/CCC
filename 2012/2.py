aromatic_number = input()
dic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
numlist = []
prevs_R = 10000
for i in range(0, len(aromatic_number),2):
    num = aromatic_number[i: i+2]
    A = int(num[0])
    R = num[1]
    R_i = dic[R]
    if prevs_R < R_i:
        numlist[-1] *= -1
    prevs_R = R_i
    numlist.append(A*R_i)
print(sum(numlist))