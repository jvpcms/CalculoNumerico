k1 = 50000
k2 = 40
m = 90
g = 9.81
h = 0.45


def func(d):

    ans = (2*k2/5) * (d**(5/2))
    ans += (k1/2) * d*d
    ans -= m*g*d + m*g*h

    return ans


def bissec(a, b, f, erro=1e-8):
    import numpy

    if numpy.sign(f(a)) == numpy.sign(f(b)):
        raise Exception(
            "The scalars a and b do not bound a root")

    c = (a + b) / 2

    if numpy.abs(a - b) < erro:
        return c

    elif numpy.sign(f(a)) == numpy.sign(f(c)):
        return bissec(c, b, f, erro)

    elif numpy.sign(f(b)) == numpy.sign(f(c)):
        return bissec(a, c, f, erro)


print(bissec(0, 0.5, func))
