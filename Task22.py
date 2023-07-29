from random import randint
print (list_n := [randint (1, 20) for i in range (1, 10)])
print (list_m := [randint (1, 20) for i in range (1, 10)])
list_total = (list_n) + (list_m)
print (set (list_total))
