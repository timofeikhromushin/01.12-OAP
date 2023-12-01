from fractions import Fraction

a = int(input("Введите числитель первой дроби: "))
b = int(input("Введите знаменатель первой дроби: "))
c = int(input("Введите числитель второй дроби: "))
d = int(input("Введите знаменатель второй дроби: "))

frac1 = Fraction(a, b)
frac2 = Fraction(c, d)

result = frac1 * frac2

print(f"Результат: {result.numerator}/{result.denominator}")