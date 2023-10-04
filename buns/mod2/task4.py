bin_num = ''
oct_num = ''
hex_num = ''

n = input()
if int(float(n)) == float(n):
    temp = int(n)
    while temp > 0:
        bin_num += str(temp % 2)
        temp //= 2
    bin_num = bin_num[::-1]

    temp = int(n)
    while temp > 0:
        oct_num += str(temp % 8)
        temp //= 8
    oct_num = oct_num[::-1]

    temp = int(n)
    alph = 'ABCDEF'
    while temp > 0:
        temp_num = temp % 16
        if temp_num < 10:
            hex_num += str(temp_num)
        else:
            temp_num = int(temp_num) - 10
            hex_num += alph[temp_num]
        temp //= 16
    hex_num = hex_num[::-1]
    if int(n) != 0:
        print(bin_num, oct_num, hex_num, sep=', ')
    else:
        print(0, 0, 0, sep=', ')
else:
    print('Неверный ввод')
