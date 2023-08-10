"""
seja f(x) a função em análise, tome f(x) = 0 e ajuste a equação
de modo a obter g(x) = x, pode haver várias formas
g(x) precisa ser escolhida de modo que:
- g(x) e g'(x) sejam contínuas no intervalo
- |g'(x)| < M < 1 em todo o intervalo
"""


def fix_point(x0, f, erro, it):

    x_prev = x0

    for i in range(it):
        x0 = f(x0)

        if float(x_prev) / x0 < erro:
            break

        x_prev = x0
