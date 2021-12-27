#Даны две переменные целого типа: A и B. 
#Если их значения не равны, то присвоить каждой переменной большее из этих значений, а если равны, то присвоить переменным нулевые значения. 
#Вывести новые значения переменных A и B.
print("Введите переменную А:")
a = int(input())
print("Введите переменную B:")
b = int(input())
if a == b:
  a = 0 
  b = 0
  print("Переменная A =", a, ", переменная B =", b)
elif a > b:
  b = a
  print("Переменная A =", a, ", переменная B =", b)
else:
  a = b
  print("Переменная A =", a, ", переменная B =", b)

#Даны три числа. Найти сумму двух наибольших из них.
s = []
print("Введите переменную А:")
s.append(float(input()))
print("Введите переменную B:")
s.append(float(input()))
print("Введите переменную C:")
s.append(float(input()))
s.sort()
print(s[1] + s[2])

#На плоскости расположены три точки: A, B, C. 
#Определить, какая из двух последних точек (B или C) расположена ближе к A, и вывести эту точку и ее расстояние от точки A.
print("Введите Сторону А: ")
a = float(input())
print("Введите Сторону B: ")
b = float(input())
print("Введите Сторону C: ")
c = float(input())
print(abs(a - b))
print(abs(a - c))
if abs(a - b) > abs(a - c):
    c = abs(a - c)
    print("Точка С ближе к точке А и их расстояние между друг другом равно,", c)
elif abs(a - c) > abs(a - b):
    b = abs(a - b)
    print("Точка B ближе к точке А и их расстояние между друг другом равно,", b)
else:
    print("Точки В и С равноудалены от точки А")

#Даны координаты точки, не лежащей на координатных осях OX и OY. Определить номер координатной четверти, в которой находится данная точка.
print("Введите координату X: ")
x = float(input())
print("Введите координату Y: ")
y = float(input())
if x > 0:
  if y > 0:
    print("Точка находится в первой плоскости")
  else:
    print("Точка находится в четвертой плоскости")
else:
  if y > 0:
    print("Точка находится во второй плоскости")
  else:
    print("Точка находится в третьей плоскости")

#Дано целое число. Вывести его строку-описание вида «отрицательное четное число», «нулевое число», «положительное нечетное число» и т. д.
print("Введите число:")
a = int(input())
if a > 0:
   if a % 2 == 0:
       print(a, "- положительное четное число")
   else:
       print(a, "- положительное нечетное число")
elif a == 0:
   print(a, "- нулевое число")
else:
   if a % 2 == 0:
       print(a, "- отрицательное четное число")
   else:
       print(a, "- отрицательное нечетное число")

#Дано целое число, лежащее в диапазоне 1–999. Вывести его строку-описание вида «четное двузначное число», «нечетное трехзначное число» и т. д.
print("Введите число:")
a = int(input())
if a == 0:
   print(a, "- нулевое число")
   exit()
if a % 2 == 0:
    print(a," - четное ", end='')
else:
    print(a, " - нечетное ", end='')
if a > 99 or a < -99:
    print("трехзначное число")
elif a > 9 or a < -9:
    print("двузначное число")
else:
    print("однозначное число")
