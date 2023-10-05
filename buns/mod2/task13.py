s = input()
even_num = ''
uneven_num = ''
flag = 0
for i in s:
    if flag % 2 != 0:
        even_num += i
    else:
        uneven_num += i
    flag += 1

sum_even = 0
sum_uneven = 0
for i in even_num:
    sum_even += int(i)
for i in uneven_num:
    sum_uneven += int(i)
if (3 * sum_even + sum_uneven) % 10 == 0:
    print('yes')
else:
    print('no')