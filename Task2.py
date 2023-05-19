#Задача 2: Найдите сумму цифр трехзначного числа.
num = input()
summa = sum([int(i) for i in num])
print(summa)