a = ''
n = ''
t = input()
is_new = False
for i in t:
    if i != ',':
        if is_new:
            n += i
        else:
            a += i
    else:
        is_new = True

print(chr((ord(a) + int(n) - 97) % 26 + 97))
