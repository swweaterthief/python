vowels = 'оыиауэёеюя'
s = input()
cnt_vow = 0
cnt_con = 0
for i in s:
    if i in vowels:
        cnt_vow += 1
    else:
        if i != ' ':
            cnt_con += 1
print(cnt_vow, cnt_con)