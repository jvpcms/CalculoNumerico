import matplotlib.pyplot as plt
import numpy as np


def func(y):

    ans = 2*(y**3) - 11.7*(y**2) + 17.7*y - 5
    return ans


dx = np.linspace(0, 4, 101)
dy = func(dx)
d0 = np.linspace(0, 0, 101)

plt.plot(dx, dy)
plt.plot(dx, d0)
plt.show()

# ans =~ 3.563
