#Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, . . . , 1 кг конфет.
print("Введите цену за 1 кг конфет:")
a = float(input())
n = 1
while n <= 10:
    print("Цена за", n/10, " кг конфет:", n/10*a)
    n += 1

#Дано целое число N (> 0). Найти произведение 1.1 · 1.2 · 1.3 · . . . (N сомножителей).
print("Введите число N:")
N = int(input())
a = 1
b = 1.1
ans = 1
while a <= N:
    ans = ans * b
    a += 1
    b += 0.1
print(ans)

#Дано целое число N (> 0). Найти квадрат данного числа, используя для его вычисления следующую формулу: N^2 = 1 + 3 + 5 + . . . + (2·N − 1). 
#После добавления к сумме каждого слагаемого выводить текущее значение суммы.
print("Введите число N:")
N = int(input())
X = 1
Ans = 1
print("N =", 1)
while X < 2*N - 1:
    X += 2
    Ans = Ans + X
    print("N =", Ans)

#Дано вещественное число A и целое число N (> 0). 
#Используя один цикл, найти сумму 1 + A + A^2 + A^3 + . . . + A^N
print("Введите число A:")
A = float(input())
print("Введите число N:")
N = int(input())
x = 1
Ans = 1
while x < N+1:
    Ans = Ans + A**x
    x += 1
print("Ответ равен:", Ans)

#Дано вещественное число A и целое число N (> 0). 
#Используя один цикл, найти значение выражения 1 − A + A2 − A3 + . . . ± AN . 
#Условный оператор не использовать.
print("Введите число A:")
A = float(input())
print("Введите число N:")
N = int(input())
x = 1
Ans = 1
while x < N+1:
    Ans = Ans + (A**x)*(-1)**x 
    x += 1
print("Ответ равен:", Ans)
