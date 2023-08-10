
def f_p(a, b, f, erro=1e-8, it=100):
    import numpy

    if numpy.sign(f(a)) == numpy.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    x1 = numpy.abs(f(a))
    x2 = numpy.abs(f(b))
    m = (a*x1 + b*x2) / (x1 + x2)

    if numpy.abs(a - b) < erro or it < 1:
        return m

    elif numpy.sign(f(a)) == numpy.sign(f(m)):
        return f_p(m, b, f, erro, it - 1)

    elif numpy.sign(f(b)) == numpy.sign(f(m)):
        return f_p(a, m, f, erro, it - 1)

