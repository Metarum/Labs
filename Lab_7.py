#Дано значение угла α в градусах (0 < α < 360). Определить значение этого же угла в радианах, учитывая, что 180◦ = π радианов.
print("Введите угол в градусах: ")
a = float(input())
a1 = 3.14*a/180
print("Значение угла в радианах:", a1)

#Дано значение угла α в радианах (0 < α < 2·π). Определить значение этого же угла в градусах, учитывая, что 180◦ = π радианов 
print("Введите угол в радианах: ")
a = float(input())
a1 = a*(180/3.14)
print("Значение угла в градусах: ", a1)

#Известно, что X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг этих же конфет.
print("Введите количество килограмм конфет:")
a = float(input())
print("Введите цену за данное количество конфет:")
b = float(input())
print("Введите количество килограмм, для которого необходимо посчитать цену:")
c = float(input())
price = b / a 
ans = price * c
print("Цена за 1 килограмм:", price)
print("Стоимость данного количества конфет равна:", ans)

#Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между ними S км. Определить расстояние между ними через T часов, если автомобили удаляются друг от друга. 
print("Введите скорость первого автомобиля: ")
V1 = float(input())
print("Введите скорость второго автомобиля: ")
V2 = float(input())
print("Введите расстояние между автомобилями: ")
S = float(input())
print("Введите время: ")
T = float(input())
S1 = S + V1*T + V2*T
print("Расстояние между автомобилями после заданного промежутка времени равно: ", S1)

#Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
print("Введите значение А: ")
a = float(input())
print("Введите значение B: ")
b = float(input())
if b == 0: 
  x = 0
else:
  x = (-b)/a
print("Значение искомой переменной равно:", x)

#Найти решение системы линейных уравнений вида 
#A1·x + B1·y = C1, 
#A2·x + B2·y = C2,
print("Введите значение А1: ")
A1 = float(input())
print("Введите значение B1: ")
B1 = float(input())
print("Введите значение C1: ")
C1 = float(input())
print("Введите значение A2: ")
A2 = float(input())
print("Введите значение B2: ")
B2 = float(input())
print("Введите значение C2: ")
C2 = float(input())
D = (A1 * B2) - (A2 * B1)
x = ((C1 * B2) - (C2 * B1)) / D
y = ((A1 * C2) - (A2 * C1)) / D
print("Значение х = ", x)
print("Значение y = ", y)