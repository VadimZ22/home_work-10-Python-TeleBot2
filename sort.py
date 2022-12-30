from fractions import Fraction
import calculate as c
import logger as lg



def sort(message):
    if 'j' in message:
        type_num = 'complex'
    else:
        type_num = 'rational'


    match type_num:
        case 'complex':
            exp = message.split()
            try: complex(exp[0]), complex(exp[-1])
            except: return 'Введены не верные данные!'
            if exp[1] in {'+', '-', '*', '/'}:
                res = c.calc_complex(exp)
                lg.complex_logger(exp, res)
                return res
            else:
                return 'Введены не верные данные!'

        case 'rational':
            exp = message.split()
            try: Fraction(exp[0]), Fraction(exp[-1])
            except: return 'Введены не верные данные!'
            if exp[1] in {'+', '-', '*', '/'}:
                res = c.calc_rational(exp)
                lg.rational_logger(exp, res)
                return res
            else:
                return 'Введены не верные данные!'








