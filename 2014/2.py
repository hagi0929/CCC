N = int(input())
f = input().split()
s = input().split()
distinct = list(set(f+s))
num_trans = {j: i for i, j in enumerate(distinct)}
fn = []
sn = []
pairs = {}
for i, j in zip(f, s):
    fn.append(num_trans[i])
    sn.append(num_trans[j])
for i, j in zip(fn, sn):
    if i in pairs and j in pairs:
        if i == pairs[j] and j == pairs[i]:
            pass
        else:
            print('bad')
            exit()
    elif i in pairs or j in pairs:
        print('bad')
        exit()
    else:
        if j == i:
            print('bad')
            exit()
        pairs[j] = i
        pairs[i] = j
print('good')
