A = list(map(float, input("Введите числа массива через пробел: ").split()))
N = len(A)

sum_value = 0
i = 0

while i < N:
    if i % 2 != 0:
        sum_value = sum_value + A[i]
    i = i + 1

print("Сумма элементов с нечётными индексами:", sum_value)