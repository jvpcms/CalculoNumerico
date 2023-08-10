from numpy import sin, cos


def d_area(x):

    return cos(x) - x * sin(x)


def bissec(a, b, f, erro=1e-8):
    import numpy

    if numpy.sign(f(a)) == numpy.sign(f(b)):
        raise Exception(
            "The scalars a and b do not bound a root")

    m = (a + b) / 2

    if numpy.abs(a - b) < erro:
        return m

    elif numpy.sign(f(a)) == numpy.sign(f(m)):
        return bissec(m, b, f, erro)

    elif numpy.sign(f(b)) == numpy.sign(f(m)):
        return bissec(a, m, f, erro)


print(bissec(0.7, 1, d_area))
