n = int(input("Введите N: "))

fact_value = 1
i = 1

while i <= n:
    fact_value = fact_value * i
    i = i + 1

print(n, "! =", fact_value)