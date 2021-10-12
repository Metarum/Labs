print("Введите координату x для первой точки =")
x1 = int(input())
print("Введите координату y для первой точки =")
y1 = int(input())
print("Введите координату x для второй точки =")
x2 = int(input())
print("Введите координату y для второй точки =")
y2 = int(input())
z = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
print("Расстояние между двумя точками =", z)


print("Введите точку A =")
a = float(input())
print("Введите точку B =")
b = float(input())
print("Введите точку C =")
c = float(input())
ac = abs(a - c)
bc = abs(b - c)
abc = ac + bc
print("Длинна AC =", ac)
print("Длинна BC =", bc)
print("Сумма отрезков AC и BC", abc)


print("Введите точку A =")
a = float(input())
print("Введите точку B =")
b = float(input())
print("Введите точку C =")
c = float(input())
if c > b and c > a or c < a and c < b:
    print("Точка С должна находиться между точками А и В")
else:
    ac = abs(a - c)
    bc = abs(b - c)
    abc = ac * bc
    print("Произведение отрезков AC и BC", abc)
    
    
print("Введите координаты вершин прямоугольника")
print("Введите координату x для первой вершины =")
x1 = float(input())
print("Введите координату y для первой вершины =")
y1 = float(input())
print("Введите координату x для второй вершины =")
x2 = float(input())
print("Введите координату y для второй вершины =")
y2 = float(input())
a = abs(x1 - x2)
b = abs(y1 - y2)
P = (a+b)*2 
S = a * b 
print("Периметр прямоугольника равен =", P)
print("Площадь прямоугольника равна =", S)


print("Введите координаты вершин треугольника")
print("Введите координату x для первой вершины =")
x1 = float(input())
print("Введите координату y для первой вершины =")
y1 = float(input())
print("Введите координату x для второй вершины =")
x2 = float(input())
print("Введите координату y для второй вершины =")
y2 = float(input())
print("Введите координату x для третьей вершины =")
x3 = float(input())
print("Введите координату y для третьей вершины =")
y3 = float(input())
ab = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
bc = ((x2-x3)**2 + (y2-y3)**2) ** 0.5
ac = ((x1-x3)**2 + (y1-y3)**2) ** 0.5
P = ab+bc+ac 
p = P/2 
S = (p*(p - ab)*(p - ac)*(p - bc)) ** 0.5
print("Периметр треугольника равен =", P)
print("Площадь треугольника равна =", S)
