import matplotlib.pyplot as plt
import numpy as np
from numpy import sign

Q = 20
g = 9.81


def func(y):

    a = (3*y + y*y*0.5)**3
    b = y + 3

    ans = Q*Q*b / (g*a)

    return 1 - ans


dx = np.linspace(1, 3, 101)
dy = func(dx)
d0 = np.linspace(0, 0, 101)

plt.plot(dx, dy)
plt.plot(dx, d0)
plt.show()

# ans =~ 1.514
