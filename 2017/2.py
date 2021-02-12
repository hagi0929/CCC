N = int(input())
sortedlst = sorted(list(map(int, input().split())), reverse=True)
first = sortedlst[N//2:]
sec = list(reversed(sortedlst[:N//2]))
i=0
while 1:
    try:
        print(first[i], sec[i], end=' ')
    except:
        try:
            print(first[i], end=' ')
        except:
            break
        break
    i += 1