# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

nb = int(input("nb = "))
def negafib(nb):
	if nb  == -1:
		return 1
	elif nb == -2:
		return -1
	else:
		return negafib(nb + 2) - negafib(nb + 1)

def posifib(nb):
	if nb == 1:
		return 0
	elif nb == 2:
		return 1
	else:
		return posifib(nb - 1) + posifib(nb - 2)


for i in range(-nb, nb + 2):
	if i < 0:
		print(negafib(i))
	elif i > 0:
		print(posifib(i))
