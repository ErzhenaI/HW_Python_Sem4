from random import randint
number = list (randint(1, 5) for i in range (int (input ('Введите количество кустов: '))))
print (number)
num = int (input ('Введите номер куста: '))
sum = 0
if num == 1:
    sum = number[0] + number[1] + number[-1]
    if num == len(number):
        sum = number[-2] + number[-1] + number[0]
else:
    sum = number[num-1] + number[num-2] + number[num]
print (sum)
