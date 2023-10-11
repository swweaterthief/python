k = int((n := int(input())) ** 0.5 // 2) + 1
t = 2 * k
d = t ** 2 - n
x, y = [k - d, -k, -k, k][d // t], [-k, -k + d - t, k, k - d + 3 * t][d // t]
print(x, y)