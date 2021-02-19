from sys import stdin
input = stdin.readline

N = int(input())
lights = []
for i in range(N):
    lights.append(int(input()))
first = lights[0]
print(lights)
current = first
counter_list = []
if first == 1:
    counter_list.append(0)
counter = 0
for i in lights:
    if i == current:
        counter += 1
    else:
        counter_list.append(counter)
        current = i
        counter = 1
counter_list.append(counter)

print(counter_list)