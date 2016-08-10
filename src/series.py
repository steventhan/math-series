# -*- coding: utf-8 -*-
'''
This module defines functions that implement mathematical series
'''


def fibonacci(n):
    '''
    returns the nth value of the fibonacci series
    '''
    if n < 0:
        return False
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    '''
    returns the nth value of the lucas series
    '''
    if n < 0:
        return False
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    '''
    returns nth value of fibonacci series if only n is passed and returns other
    series if n passed as nth value, and a, b are passed as the series'
    starting points
    '''
    if n < 0:
        return False
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)


def main():
    print(__doc__)
    print(u'fibonacci(n)', fibonacci.__doc__)
    print(u'>>> fibonacci(7)')
    print(fibonacci(7), end='\n\n')
    print(u'lucas(n)', lucas.__doc__)
    print(u'>>> lucas(5)')
    print(lucas(5), end='\n\n')
    print(u'sum_series(n, a, b)', sum_series.__doc__)
    print(u'>>> sum_series(10)')
    print(sum_series(10), end='\n\n')
    print(u'>>> sum_series(8, 9, 10)')
    print(sum_series(8, 9, 10), end='\n\n')

if __name__ == '__main__':
    main()
