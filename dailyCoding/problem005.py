#########################################################################################
# Problem 5 : medium
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Jane Street.
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
# returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.
#########################################################################################



#This is an example of functional programming
# functional you have a function (interface) that 
# accepts another function (implementation) and calls it inside.

#Ref : https://galaiko.rocks/posts/dcp/problem-5/


def cons(a, b):
    return lambda f: f(a, b)

def car(f):
    z = lambda x, y: x
    return f(z)

def cdr(f):
    z = lambda x, y: y
    return f(z)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
