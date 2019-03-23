"""
Stone Yun 2019.
For any number n > 1, will find how many operations it takes to get to 1 as described in README
"""
import numpy as np
from helpers import args
from step import *


def run_collatz(num):
    steps = 0
    #TODO: create decorators that will count when the step functions are called
    while num != 1:
        if num%2 == 1:
            num = step_odd(num)
        else:
            num = step_even(num)
        steps += 1
    return steps

if __name__ == "__main__":
    args.add_arg('-n','--number', required=True)
    num = int(args.get_arg('number'))
    s = run_collatz(num)
    print(f"Starting from {num} it took {s} steps to get to 1")
