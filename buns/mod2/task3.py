def midl_count_1():
    s = input()
    variables = ['a', 'b', 'c']
    values = {}

    i = 0
    for char in s:
        if char != ' ':
            values[variables[i]] = int(char)
            i += 1
            if i == 3:
                break

    a = values.get('a')
    b = values.get('b')
    c = values.get('c')

    if (a, b, c > 0):
        if (a < b and b < c) or (c < b and b < a):
            return(b)
        elif (b < a and a < c) or (c < a and a < b):
            return(a)
        else:
            (a < c and c < b) or (b < c and c < a)
            return(c)
    return(c)

print(midl_count_1())