def get_armstrong_numbers():
    num = 10
    while True:
        if num == sum(int(digit) ** len(str(num)) for digit in str(num)):
            yield num
        num += 1

armstrong_numbers = get_armstrong_numbers()
for _ in range(8):
    print(next(armstrong_numbers), end=' ')