s = input()
a = ''
b = ''
c = ''
cnt = 0
for i in s:
    if i != '.':
        if cnt == 0:
            a += i
        elif cnt == 1:
            b += i
        else:
            c += i
    else:
        cnt += 1

print(c)
print(b)
print(a)
