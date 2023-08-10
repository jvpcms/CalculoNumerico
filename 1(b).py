import matplotlib.pyplot as plt
import numpy as np
from numpy import sign

Q = 20
g = 9.81


def func(y):

    a = (3*y + y*y*0.5)**3
    b = y + 3

    ans = Q*Q*b / (g*a)

    return 1 - ans


def bissec(a, b, f, erro=1e-8, it=100):
    import numpy

    if numpy.sign(f(a)) == numpy.sign(f(b)):
        raise Exception(
            "The scalars a and b do not bound a root")

    m = (a + b) / 2

    if numpy.abs(b - a) < erro or it <= 1:
        return m

    elif numpy.sign(f(a)) == numpy.sign(f(m)):
        return bissec(m, b, f, erro, it - 1)

    elif numpy.sign(f(b)) == numpy.sign(f(m)):
        return bissec(a, m, f, erro, it - 1)


print(bissec(0.5, 2.5, func, erro=0.01, it=10))

# ans =~ 1.514
