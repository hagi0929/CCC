from guppy import hpy; h=hpy()
import sys
N = input()
H = input()
N_len = len(N)
H_len = len(H)
N_dic = {}
H_f_dic = {}
ans_dic = {}
ans = []
letter_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
if N_len > H_len:
    print(0)
    exit()

for ltr in letter_lst:
    N_dic[ltr] = 0
    H_f_dic[ltr] = 0

for N_i, H_i in zip(N, H[:N_len]):
    N_dic[N_i] += 1
    H_f_dic[H_i] += 1
for ltr_d, N_N, H_H in zip(N_dic.keys(), N_dic.values(), H_f_dic.values()):
    ans_dic[ltr_d] = H_H - N_N

if not any(ans_dic.values()):
    ans.append(H[:N_len])

for n in range(N_len, H_len):
    end = n
    start = n - N_len
    ans_dic[H[end]] += 1
    ans_dic[H[start]] -= 1
    if not any(ans_dic.values()):
        if H[start + 1: end + 1] not in ans:
            ans.append(H[start + 1: end + 1])


print(len(ans))

print(h.heap())
print(f"N: {sys.getsizeof(N)}")
print(f"H: {sys.getsizeof(H)}")
print(f"N_len: {sys.getsizeof(N_len)}")
print(f"H_len: {sys.getsizeof(H_len)}")
print(f"N_dic: {sys.getsizeof(N_dic)}")
print(f"H_f_dic: {sys.getsizeof(H_f_dic)}")
print(f"ans_dic: {sys.getsizeof(ans_dic)}")
print(f"ans: {sys.getsizeof(ans)}")
print(f"letter_lst: {sys.getsizeof(letter_lst)}")
