'''
This module is used to complex math calculation.
'''

def percentage(obt, tot):
    '''
    '''
    if obt > tot:
        obt , tot = tot , obt
    return obt / tot * 100


def factorial(n):
    '''
    '''
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact

