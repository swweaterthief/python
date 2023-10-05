s_input = input()
s = ''
i_s = ''

is_new_num = False
for i in s_input:
    if i != ',':
        if is_new_num:
            i_s += i
        else:
            s += i
    else:
        is_new_num = True

answer = 0
for i in s:
    if i == i_s:
        answer += 1
    else:
        break

print(answer)
