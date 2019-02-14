#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The main goals of these katas are:

get you used to writing and calling functions that take arguments and return results in Python
get you used to breaking down a problem into the various parts of a for loop in Python """

__author__ = "dougenas"

# add function


def add(x, y):
    return x + y


print("Add " + str(add(2, 4)))

# multiply function


def multiply(x, y):
    product = 0
    for i in range(y):
        product = add(product, x)
    return product


print("Multiply " + str(multiply(6, 8)))

# power function


def power(a, n):
    for i in range(1, n+1):
        product = multiply(i, a)
    return product * product


print("Power " + str(power(2, 8)))

# factorial function


def factorial(n):
    product = 1
    for i in range(1, n+1):
        product = multiply(product, i)
    return product


print("Factorial " + str(factorial(4)))

# fibonacci function


def fibonacci(n):
    n1 = 0
    n2 = 1
    product = 1
    for i in range(3, n+1):
        product = add(n1, n2)
        n1 = n2
        n2 = product
    return product


print("Fibonacci " + str(fibonacci(8)))
