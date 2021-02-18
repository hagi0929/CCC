from sys import stdin
input = stdin.readline
N = int(input())
correct_answer = []
for i in range(N):
    rcv =input().rstrip()
    correct_answer.append(rcv)

student_answer = []
for i in range(N):
    rcv =input().rstrip()
    student_answer.append(rcv)
score = 0
for i, j in zip(correct_answer, student_answer):
    if i == j:
        score += 1
print(score)