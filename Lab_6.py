//Поменять местами содержимое переменных A и B и вывести новые значения A и B.
print("Введите переменную A = ")
a = float(input())
print("Введите переменную B = ")
b = float(input())
a = a + b
b = a - b 
a = a - b 
print("Значение переменной А = ", a)
print("Значение переменной B = ", b)

//Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A, и вывести новые значения переменных A, B, C.
print("Введите переменную A = ")
a = float(input())
print("Введите переменную B = ")
b = float(input())
print("Введите переменную C = ")
c = float(input())
a = a + b
b = a - b 
a = a - b 
a = a + c
c = a - c 
a = a - c 
print("Значение переменной А = ", a)
print("Значение переменной B = ", b)
print("Значение переменной C = ", c)

//Даны переменные A, B, C. Изменить их значения, переместив содержимое A в C, C — в B, B — в A, и вывести новые значения переменных A, B, C.
print("Введите переменную A = ")
a = float(input())
print("Введите переменную B = ")
b = float(input())
print("Введите переменную C = ")
c = float(input())
a = a + c
c = a - c 
a = a - c 
b = b + a
a = b - a
b = b - a 
print("Значение переменной А = ", a)
print("Значение переменной B = ", b)
print("Значение переменной C = ", c)

//Найти значение функции y = 3x^6 − 6x^2 − 7 при данном значении x
print("Функция равна 3x^6 − 6x^2 − 7. Введите переменную x, чтобы рассчитать функцию = ")
x = float(input())
y = 3*x**6 - 6*x**2 - 7
print("Значение функции y = ", y)

//Найти значение функции y = 4(x−3)^6 − 7(x−3)^3 + 2 при данном значении x
print("Функция равна 4(x−3)^6 − 7(x−3)^3 + 2. Введите переменную x, чтобы рассчитать функцию = ")
x = float(input())
y = 4*(x - 3)**6 - 7*(x - 3)**3 + 2
print("Значение функции y = ", y)

//Дано число A. Вычислить A^8 , используя вспомогательную переменную и три операции умножения.
print("Введите число A = ")
a = float(input())
a1 = a
a = a*a 
a = a*a 
a = a*a
print(a1, "в восьмой степени равняется ", a)

//Дано число A. Вычислить A^15, используя две вспомогательные переменные и пять операций умножения
print("Введите число A = ")
a = float(input())
a1 = a
x = a*a
a = x*a
a = x*a
x = a*a
a = x*a
print(a1, "в пятнадцатой степени равняется ", a)
