def check_parity(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return check_parity(a * a, n//2)
    else:
        return a * check_parity(a, n-1)

a, n = map(int, input().split())
print(check_parity(a, n))