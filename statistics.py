#! /home/toni/.pyenv/shims/python3
"""
Created on Oct 29, 2020

@author:toni

Calculate the probability distribution of a sequence of tasks.
The estimate may either be in hours or days.
"""

import math


def estimate(o, n, p):
    """Return estimate of a task.
    
    o -- integer or float, optimistic estimate
    n -- integer or float, nominal estimate
    p -- integer or float, pessimistic estimate
    
    returns: float
    """
    if o <= 0 or n <= 0 or p <= 0:
        raise ValueError
    if o > n or n > p:
        raise ValueError
    return (o + 4*n + p)/6


def probability(*args):
    """Return the probability distribution of a series of tasks.
    
    args -- tuples of 3 floats, (o, n, p).
    
    returns: float
    """
    return sum((estimate(*arg) for arg in args))


def stddev(o, p):
    """
    Return standard deviation.
    """
    if o <= 0 or p <= 0:
        raise ValueError
    if o > p:
        raise ValueError
    return (p-o) / 6


def seq_stddev(*args):
    """Return standard deviation of sequence of tasks.
    
    args -- tuples of two floats, (o, p)
    
    returns: float"""
    return math.sqrt(sum((stddev(*arg)**2 for arg in args)))


def final_estimate(*args):
    """Return the final estimate for a sequence of tasks.
    
    args -- tuples of 3 floats, (o, n, p)
    
    returns: float
    """
    if not all((isinstance(e, (int, float)) for arg in args for e in arg)):
        raise ValueError
    onp = args
    op = tuple((arg[0], arg[-1]) for arg in args)
    est = probability(*onp)
    sig = seq_stddev(*op)
    return est + sig


def main():
    print(final_estimate((1, 3, 12), (1, 1.5, 14), (3, 6.25, 11)))


if __name__ == "__main__":
    main()
