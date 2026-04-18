A = list(map(int, input("Введите целые числа массива через пробел: ").split()))
N = len(A)

sum_value = 0
i = 0

while i < N:
    if A[i] % 2 != 0:
        sum_value = sum_value + A[i]
    i = i + 1

print("Сумма нечётных элементов:", sum_value)