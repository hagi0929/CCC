letter_list = ['A', 'B', 'C']
ABC = {
    'A': 0,
    'B': 0,
    'C': 0,
}
pattern = [0]
N = input()
selector = 0
for n in N:
    ABC[n] += 1
    while True:
        if n == letter_list[selector%3]:
            pattern[selector] += 1
            break
        else:
            pattern.append(0)
            selector += 1
print(sorted(N))
print(pattern)