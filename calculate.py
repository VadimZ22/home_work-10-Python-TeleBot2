from fractions import Fraction

def calc_complex(exp):
    a, b, c = exp
    match b:
        case '+':
            return complex(a) + complex(c)
        case '-':
            return complex(a) - complex(c)
        case '*':
            return complex(a) * complex(c)
        case '/':
            return complex(a) / complex(c)

def calc_rational(exp):
    a, b, c = exp
    match b:
        case '+':
            return Fraction(a) + Fraction(c)
        case '-':
            return Fraction(a) - Fraction(c)
        case '*':
            return Fraction(a) * Fraction(c)
        case '/':
            return Fraction(a) / Fraction(c)

