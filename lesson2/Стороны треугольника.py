a=float(input('Первая сторона '))
b=float(input('Вторая сторона '))
c=float(input('Третья сторона '))
p=(a+b+c)/2
print('Полупериметр ',p)
P=p*(p-a)*(p-b)*(p-c)
print('Периметр ',P)
S=P**0.5
print('Площадь ',S)
