import math


class Fraction:
    def __init__(self, numerator, denominator):
        try:
            numerator = int(numerator)
        except ValueError:
            raise ValueError('Numerator of a fraction should be an integer.')

        try:
            denominator = int(denominator)
        except ValueError:
            raise ValueError('Denominator of a fraction should be an integer.')

        if denominator == 0:
            raise ValueError('Fraction cannot have denominator equals to 0.')

        self._numerator, self._denominator = self._get_simplified(numerator, denominator)

    @staticmethod
    def _get_simplified(numerator, denominator):
        gcd = math.gcd(numerator, denominator)  # Greatest Common Divisor
        return numerator // gcd, denominator // gcd

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def __add__(self, other):
        # lcm will be the denominator of the resulted fraction
        lcm = math.lcm(self._denominator, other.denominator)  # Lowest Common Multiple
        first_fraction_numerator = self._numerator * (lcm // self._denominator)
        second_fraction_numerator = other.numerator * (lcm // other.denominator)

        return Fraction(first_fraction_numerator + second_fraction_numerator, lcm)

    def __sub__(self, other):
        pass

    def inverse(self):
        return Fraction(self._denominator, self._numerator)

    def __str__(self):
        return f'{self._numerator}/{self._denominator}'


if __name__ == '__main__':
    # x = 5
    # y = 7
    # z = x + y
    # print('z', z)
    #
    # a = 'ana '
    # b = 'are '
    # c = 'mere'
    # r = a + b + c
    # print('r', r)

    # x = Fraction(1, 5)
    # print('x', x)
    #
    # y = Fraction(2, 5)
    # print('y', y)
    #
    # z = x + y
    # print('z', z)

    # x = Fraction(2, 4)  # 1/2
    # y = Fraction(3, 8)  # 3/8
    # z = x + y + Fraction(1, 8)  # 4/8 + 3/8 = 7/8
    # print('z', z, type(z))

    x = Fraction(3, 4)
    print('x', x)
    y = x.inverse()
    print('y', y)
