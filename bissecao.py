
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

