# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
ticket = str(input())
while (len(ticket) !=6):
    print("Количество символов не соответствует условию задачи. Попробуйте еще раз")
    ticket = str(input())
count=0
for i, val in enumerate(ticket):
    if i <=2: count+=int(val)   
    else: count-=int(val)        
print('Yes' if (count == 0) else 'No')
