# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
n = int(input("Input N: "))
print("Input list digits: ")
my_list = [int(input()) for i in range(n)]
x = int(input("Input X: "))
print(my_list.count(x) if my_list.count(x) else "No")