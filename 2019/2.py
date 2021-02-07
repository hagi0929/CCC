def solution(n):
    sieve = [True] * (n + 1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n + 1) if sieve[i] == True]
ii = []
N = int(input())
for _ in range(N):
    ii.append(int(input()))

prime_numbers = solution(max(ii)*2)

len = len(prime_numbers)
for i in ii:
    result = i * 2
    for j in range(int(min(ii)/len), len):
        if i <= prime_numbers[j]:
            start = j
            break
    left = int(start/2)+1
    right = int(start/2)+1
    while 1:
        if result == prime_numbers[left] + prime_numbers[right]:
            print(prime_numbers[left], prime_numbers[right])
            break
        elif result > prime_numbers[left] + prime_numbers[right]:
            left += 1
        elif result < prime_numbers[left] + prime_numbers[right]:
            right -= 1