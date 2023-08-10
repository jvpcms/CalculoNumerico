import numpy


def search(x1, x2, dx, func):

    while x1 <= x2:

        if numpy.sign(func(x1)) != numpy.sign(func(x1 + dx)):
            return x1, x1 + dx

        else:
            x1 += dx


