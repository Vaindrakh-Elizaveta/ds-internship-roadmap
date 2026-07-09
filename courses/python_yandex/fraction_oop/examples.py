from fraction import Fraction


a = Fraction(1, 3)
b = Fraction(1, 2)

print("a =", a)
print("b =", b)

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)

c = Fraction("-3/9")
print("c =", c)
print("-c =", -c)
print("c.reverse() =", c.reverse())

d = Fraction(2)
print("d =", d)
print("a + 2 =", a + 2)
print("2 + a =", 2 + a)
print("2 - a =", 2 - a)
print("2 / a =", 2 / a)