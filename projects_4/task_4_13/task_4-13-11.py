A = list(map(float, input("Введите числа массива через пробел: ").split()))
N = len(A)

sum_value = 0
count_value = 0
i = 0

while i < N:
    if i % 2 == 0:
        sum_value = sum_value + A[i]
        count_value = count_value + 1
    i = i + 1

if count_value > 0:
    average_value = sum_value / count_value
else:
    average_value = 0

print("Среднее арифметическое элементов с чётными индексами:", average_value)