A = list(map(float, input("Введите числа массива через пробел: ").split()))
N = len(A)

sum_value = 0
i = 0

while i < N:
    sum_value = sum_value + A[i]
    i = i + 1

average_value = sum_value / N

print("Среднее арифметическое:", average_value)