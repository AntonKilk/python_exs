# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from curses.ascii import isdigit

N = input('N = ')
sum = 0
for digit in N:
	if  isdigit(digit):
		sum += int(digit)
print(sum)
