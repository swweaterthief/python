def common_divisor(a, b):
    if b == 0:
        return a
    else:
        return common_divisor(b, a % b)

a, b = map(int, input().split())
print(common_divisor(a, b))