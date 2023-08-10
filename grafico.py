
def plt(x1, x2, f, n=100):

    import matplotlib.pyplot
    import numpy

    dx = numpy.linspace(x1, x2, n)
    dy = f(dx)

    matplotlib.pyplot.plot(dx, dy)
    matplotlib.pyplot.show()

