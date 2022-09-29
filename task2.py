#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = 1
Y = 2
Z = 3
a = not(X or Y or Z)
b = (not X) and (not Y) and (not Z)
print(a == b)
