N = sorted(input())
H = input()
l = len(N)
i=0
ans = 0
f_ans = []
len_h = len(H)
len_n = len(N)


def method1(init):
    for i in range(init, len_h - len_n + 1):
        ans = H[i:i + l]
        ans_inv = sorted(ans)
        add = True
        print(i)
        if set(ans) == set(N):
            for j in range(len_n):
                if N[j] != ans_inv[j]:
                    add = False
                    break
        else:
            add = False
            pass
        if add:
            print('d')
            f_ans.append(ans)
            return i



def method2(init):
    if init:
        remove_lst = []
        add_lst = []
        for i in range(init + 1, len_h - len_n):
            remove_lst.append(H[i])
            add_lst.append(H[i + len_n])
            print(i)
            if sorted(remove_lst) == sorted(add_lst):
                f_ans.append(H[i+1:i + len_n+1])
                print(i)
                remove_lst = []
                add_lst = []
            if len(remove_lst) >= 1000:
                for o, p in zip(add_lst, remove_lst):

                return i


init_main = 0
while True:
    init_main = method1(init_main)
    init_main = method2(init_main)
    print(i)
    if not init_main:
        break

print(len(set(f_ans)))