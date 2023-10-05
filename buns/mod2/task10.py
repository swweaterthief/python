s = input()
answer = ''
a = ''
for i in s:
    if i == ' ':
        answer += a
    a = i
answer += a
print(answer)