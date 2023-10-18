def palindrome(s):
    counts = [0] * 256
    for char in s:
        counts[ord(char)] += 1

    another_count = 0
    for count in counts:
        if count % 2 != 0:
            another_count += 1

    if another_count > 1:
        return "Невозможно составить палиндром"

    first_part = [chr(i) * (counts[i] // 2) for i in range(256) if counts[i] > 0]
    second_part = first_part.copy()
    second_part.reverse()
    middle = [chr(i) for i in range(256) if counts[i] % 2 != 0]

    return ''.join(first_part + middle + second_part)

s = input()
print(palindrome(s))
