Y = int(input())
for i in range(Y+1, 100000):
    if sorted(list(str(i))) == sorted(list(set(list(str(i))))):
        print(i)
        exit()
