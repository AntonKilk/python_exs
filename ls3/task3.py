# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

import math

list = [1.11, 1.2, 3.1, 5, 10.01]

l = len(list)
deci = [0] * l
k = 0
for i in list:
	deci [k] = (round(i % 1, 2))
	k += 1

lowest = 99999999
highest = max(deci)
for i in deci:
	if i != 0:
		if lowest > i:
			lowest = i

print(highest - lowest)
