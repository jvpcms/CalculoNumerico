
def func(y):

    ans = 2*(y**3) - 11.7*(y**2) + 17.7*y - 5
    return ans


def d_func(y):

    ans = 6*(y**2) - 23.4*y + 17.7
    return ans


def n_r(x, it=3):
    x = x - func(x) / d_func(x)

    if it == 0:
        return x

    return n_r(x, it - 1)


print(n_r(3))
