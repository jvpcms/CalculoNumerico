
def sec(x0, x1, f, it=200, erro=1e-8):

    x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))

    if abs(f(x2)) < erro or it <= 0:
        return x2
    if abs(f(x2)) > abs(f(x1)):
        return "não converge"

    return sec(x1, x2, f, it - 1)
