s = input()
a = ''
flag = True
for i in s:
    if i in a:
        print(True)
        flag = False
        break
    if i != ' ':
        a += i

if flag:
    print(False)
