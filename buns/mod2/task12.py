s = input()
flag = '-)( '
answer = ''
for i in s:
    if not (i in flag):
        answer += i
print(answer)