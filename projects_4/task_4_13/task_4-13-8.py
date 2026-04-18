A = list(map(float, input("Введите числа массива через пробел: ").split()))
N = len(A)

count_value = 0
i = 0

while i < N:
    if A[i] > 0:
        count_value = count_value + 1
    i = i + 1

print("Количество положительных чисел:", count_value)