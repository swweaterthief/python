def check_input(numbers):
    if len(set(numbers)) == 1:
        return "Все числа равны"
    elif len(set(numbers)) == len(numbers):
        return "Все числа не равны"
    else:
        return "Есть равные и неравные числа"

numbers = list(map(int, input().split()))
print(check_input(numbers))