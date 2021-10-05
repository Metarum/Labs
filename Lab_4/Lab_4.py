a = float(input('Сторона a:')) 
b = float(input('Сторона b:'))
S = a*b
P = 2*(a + b)
print("S =", S)
print("P =", P)

d = float(input('Диаметр d:')) 
π = 3.14
L = π*d 
print("L =", L)

a = float(input('Число a:')) 
b = float(input('Число b:'))
sr = ((a+b)/2)
print("Среднее арифметическое =", sr)

a = float(input('Число a:')) ** 2
b = float(input('Число b:')) ** 2
sm = a + b
rz = a - b
pr = a * b 
ch = a / b
print("Сумма квадратов a и b =", sm)
print("Разность квадратов a и b =", rz)
print("Произведение квадратов a и b =", pr)
print("Частное квадратов a и b =", ch)

a = abs(float(input('Число a:')))
b = abs(float(input('Число b:')))
sm = a + b
rz = a - b 
pr = a * b 
ch = a / b 
print("Сумма модулей a и b =", sm)
print("Разность модулей a и b =", rz)
print("Произведение модулей a и b =", pr)
print("Частное модулей a и b =", ch)
