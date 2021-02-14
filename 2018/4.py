num = 1
n = int(input())
BalTreeCount = {}

BalTreeCount[1] = 1


def trees(n):
    if n in BalTreeCount:  # Checks if value already calculated
        return BalTreeCount[n]
    else:
        tot = 0

        for i in range(2, n + 1):  # i represents number of branches
            a = n // i  # a is weight, weight of root divided among the branches
            print(n, a, i)
            if a in BalTreeCount:  # If value calculated, use that
                tot += BalTreeCount[a]
            else:  # Else recalculate value
                tot += trees(a)

        BalTreeCount[n] = tot  # Record new value
        print(BalTreeCount)
        return tot  # Return it to be used


print(trees(n))