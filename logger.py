from datetime import datetime as dt
from time import time

def complex_logger(exp, res):
    time = dt.now().strftime('%D,%H,%M')
    with open('log.csv', 'a') as file:
        file.write('{}, complex operation, {}, = {}\n'.format(time, exp, res))
    return

def rational_logger(exp, res):
    time = dt.now().strftime('%D,%H,%M')
    with open('log.csv', 'a') as file:
        file.write('{}, rational operation, {}, = {}\n'.format(time, exp, res))
    return

