# F = 1.25
# x =~ 0.2 ou 1.2 pelo gráfico

e = 8.85 * 1e-12
pi = 3.14
q = 2 * 1e-5
r = 0.9


def force(x):

    ans = q*q*x / (4*pi*e)
    ans /= (x*x + r*r) ** (3/2)

    return ans - 1.25


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


print(bissec(0.1, 0.3, force))
print(bissec(1.1, 1.3, force))
