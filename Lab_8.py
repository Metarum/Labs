#Дан размер файла в байтах. Найти количество полных килобайтов, которые занимает данный файл
print("Введите количество байт: ")
a = int(input())
a1 = a // 1024
print("Количество килобайт:", a1)

#Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). 
#Найти количество отрезков B, размещенных на отрезке A.
print("Введите число А: ")
a = int(input())
print("Введите число В: ")
b = int(input())
a1 = a // b
print("Количество отрезков В на отрезке А:", a1)

#Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). 
#Найти длину незанятой части отрезка A.
print("Введите число А: ")
a = int(input())
print("Введите число В: ")
b = int(input())
a1 = a - (a // b) * b
print("Длина незанятой части отрезка А:", a1)

#Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.
print("Введите двузначное число: ")
a = int(input())
a1 = a // 10 + a % 10 * 10
print("Число, полученное после перестановок цифр:", a1)

#Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее справа. Вывести полученное число.
print("Введите трехзначное число: ")
a = int(input())
a1 = (a % 100 * 10) + (a // 100)
print("Число, полученное после перестановок цифр:", a1)
