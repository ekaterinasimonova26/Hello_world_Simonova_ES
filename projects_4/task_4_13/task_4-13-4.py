n = int(input("Введите N: "))

sum_value = 0
i = 1

while i <= n:
    sum_value = sum_value + i
    i = i + 1

print("Сумма чисел от 1 до", n, "=", sum_value)