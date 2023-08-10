pi = 3.14
r = 3


def v(h):

    ans = pi*h*h * (3*r - h) / 3
    return ans - 30


def d_v(h):

    ans = pi * (2*r*h - h*h)
    return ans


def n_r(x0, f, df, it=200, erro=1e-8):

    x1 = x0 - f(x0) / df(x0)

    print(f"x: {x1}, erro relativo: {(abs((x1 - x0) / x0))}")

    if it <= 1 or abs(f(x1)) < erro:
        return x1

    return n_r(x1, f, df, it - 1)


print(n_r(1, v, d_v, 3))
