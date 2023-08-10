
def n_r(x0, f, df, it=200, erro=1e-8):

    x1 = x0 - f(x0) / df(x0)

    if it <= 1 or abs(f(x1)) < erro:
        return x1

    return n_r(x1, f, df, it - 1)
