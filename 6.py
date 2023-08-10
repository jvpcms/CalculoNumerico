import numpy

Re = float(input("Insira número de Reynolds: "))


def func(f):

    ans = 4 * numpy.log10(Re*numpy.sqrt(f)) - 0.4
    ans *= numpy.sqrt(f)
    ans -= 1

    return ans


def bissec(a, b, f, erro=4e-6):
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


print(bissec(0.001, 0.015, func))
