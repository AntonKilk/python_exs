# Задайте число N, создайте список: [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода
# и зависит от количества элементов в списке) в одной строке одно число

import random

# cоздаем массив [-N, N]
N = int(input('N = '))
print('\n')
k = -N
arr = []
while k <= N:
	arr.append(k)
	k += 1
print('Массив: ')
for el in arr:
	print(el, end=' ')
print('\n')

# записываем N случайных чисел в файл file.txt:
elements = []
i = 0
while i < N:
	elements.append(random.randint(0, N * 2))
	i += 1
data = open('file.txt', 'w')

for nb in elements:
	data.write(str(nb))
	data.write("\n")
data.close()

print('Выбранные позиции массива: ')
for el in elements:
	print(el, end=' ')
print('\n')

# вывести произведение элементов массива с номерами из файла
path = 'file.txt'
d = open(path, 'r')
result = 1
for i in d:
	result *= arr[int(i)]
data.close()
print('Результат =', result)
