from numpy import linspace, sin, cos

e = 0.9
x = linspace(0, 3.14, 30)


def func(y, c):

    return y - e*sin(y) - c


def d_func(y):

    return 1 - e*cos(y)


def n_r(x0, f, df, d, it=200, erro=1e-8):

    x1 = x0 - f(x0, d) / df(x0)

    if it <= 1 or abs(f(x1, d)) < erro:
        return x1

    return n_r(x1, f, df, d, it - 1)


for i in x:
    print(f"x: {i}, y: {n_r(1.5, func, d_func, i)}")
