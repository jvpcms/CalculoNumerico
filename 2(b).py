
def func(y):

    ans = 2*(y**3) - 11.7*(y**2) + 17.7*y - 5
    ans *= 0.05
    return y - ans


def fix_point(x0, f, it=3):

    for i in range(it):
        x0 = f(x0)

    return x0


o = 3

print(fix_point(o, func))
