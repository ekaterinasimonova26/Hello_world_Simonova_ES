a = float(input("Введите число A: "))
b = float(input("Введите число B: "))
c = float(input("Введите число C: "))
d = float(input("Введите число D: "))

min_value = a

if b < min_value:
    min_value = b
if c < min_value:
    min_value = c
if d < min_value:
    min_value = d

print("Минимальное число:", min_value)