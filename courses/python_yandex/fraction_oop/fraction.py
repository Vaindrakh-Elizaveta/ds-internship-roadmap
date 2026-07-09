def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                if '/' in args[0]:
                    a, b = args[0].split('/')
                else:
                    a, b = args[0], 1
            elif isinstance(args[0], int):
                a, b = args[0], 1
        else:
            a, b = args
        if ('-' in str(a) and '-' not in str(b)) or ('-' in str(b) and '-' not in str(a)):
            self.__sign = '-'
        else:
            self.__sign = ''

        self.__numerator = abs(int(a))
        self.__denominator = abs(int(b))
        self.__reduce()

    def __reduce(self):
        g = gcd(self.__numerator, self.__denominator)
        self.__numerator //= g
        self.__denominator //= g

    def __reduction_sign(self):
        if self.__sign == '-' and (str(self.__denominator)[0] == '-' or str(self.__numerator)[0] == '-'):
            self.__sign = ''
        elif self.__sign == '' and (str(self.__denominator)[0] == '-' or str(self.__numerator)[0] == '-'):
            self.__sign = '-'

    def numerator(self, number=None):
        if number is None:
            return abs(self.__numerator)

        self.__numerator = number
        self.__reduction_sign()
        self.__numerator = abs(int(number))
        self.__reduce()

    def denominator(self, number=None):
        if number is None:
            return abs(self.__denominator)

        self.__denominator = number
        self.__reduction_sign()
        self.__denominator = abs(int(number))
        self.__reduce()

    def __to_fraction(self, other):
        if isinstance(other, Fraction):
            return other
        return Fraction(other)

    def __str__(self):
        return f'{self.__sign}{self.__numerator}/{self.__denominator}'

    def __repr__(self):
        return f'Fraction(\'{str(self)}\')'

    def __neg__(self):
        new_fraction = Fraction(self.__numerator, self.__denominator)
        if self.__sign == '-':
            new_fraction.__sign = ''
        else:
            new_fraction.__sign = '-'
        return new_fraction

    def __add__(self, other):
        other = self.__to_fraction(other)
        denominator = self.__denominator * other.__denominator
        a = int(self.__sign + str(self.__numerator * other.__denominator))
        b = int(other.__sign + str(other.__numerator * self.__denominator))
        numerator = a + b
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        other = self.__to_fraction(other)
        return self + (-other)

    def __iadd__(self, other):
        other = self.__to_fraction(other)
        c = self + other
        self.__numerator = c.__numerator
        self.__denominator = c.__denominator
        self.__sign = c.__sign
        return self

    def __isub__(self, other):
        other = self.__to_fraction(other)
        c = self - other
        self.__numerator = c.__numerator
        self.__denominator = c.__denominator
        self.__sign = c.__sign
        return self

    def __mul__(self, other):
        other = self.__to_fraction(other)
        denominator = self.__denominator * other.__denominator
        numerator = self.__numerator * other.__numerator
        new_fraction = Fraction(numerator, denominator)
        if self.__sign == other.__sign:
            new_fraction.__sign = ''
        else:
            new_fraction.__sign = '-'
        return new_fraction

    def reverse(self):
        new_fraction = Fraction(self.__denominator, self.__numerator)
        new_fraction.__sign = self.__sign
        return new_fraction

    def __truediv__(self, other):
        other = self.__to_fraction(other)
        return self * other.reverse()

    def __imul__(self, other):
        other = self.__to_fraction(other)
        c = self * other
        self.__numerator = c.__numerator
        self.__denominator = c.__denominator
        self.__sign = c.__sign
        return self

    def __itruediv__(self, other):
        other = self.__to_fraction(other)
        c = self / other
        self.__numerator = c.__numerator
        self.__denominator = c.__denominator
        self.__sign = c.__sign
        return self

    def __gt__(self, other):
        other = self.__to_fraction(other)
        new_num_self = self.__numerator * other.__denominator
        new_num_other = other.__numerator * self.__denominator
        if int(self.__sign + str(new_num_self)) > int(other.__sign + str(new_num_other)):
            return True
        else:
            return False

    def __lt__(self, other):
        other = self.__to_fraction(other)
        return not (self > other or self == other)

    def __ge__(self, other):
        other = self.__to_fraction(other)
        return self > other or self == other

    def __le__(self, other):
        other = self.__to_fraction(other)
        return not (self > other)

    def __eq__(self, other):
        other = self.__to_fraction(other)
        new_num_self = self.__numerator * other.__denominator
        new_num_other = other.__numerator * self.__denominator
        if int(self.__sign + str(new_num_self)) == int(other.__sign + str(new_num_other)):
            return True
        else:
            return False

    def __ne__(self, other):
        other = self.__to_fraction(other)
        return not (self == other)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return -self + other

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        return self.reverse() * other
