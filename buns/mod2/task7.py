s = input()
cnt_0 = 0
cnt_1 = 0

for i in s:
    if i == '0':
        cnt_0 += 1
    else:
        cnt_1 += 1

if cnt_0 == cnt_1:
    print('yes')
else:
    print('no')
