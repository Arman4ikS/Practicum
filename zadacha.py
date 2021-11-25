a = int(input())
b = int(input())
c = int(input())
if (a > 0) and (b > 0) and (c > 0) and (a+b > c) and (a+c > b) and (b+c > a):
    print("Треугольник существует")
    if (a ** 2 + b ** 2 == c ** 2):
        print("и он прямоугольный")
    elif (a ** 2 + b ** 2 < c ** 2):
        print("и он тупооугольный")
    else:
        print("и он остроугольный")
else:
    print("Треугольник не существует")

