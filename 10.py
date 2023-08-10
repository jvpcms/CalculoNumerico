# Algoritmo de Moler-Morrison

teste_x = [3, -5, 7]
teste_y = [4, 12, 24]


def moler(x, y):

    f = max(abs(x), abs(y))
    a = min(abs(x), abs(y))

    for j in range(3):
        b = (a / f) ** 2
        c = b / (b + 4)
        f = f + 2 * c * f
        a = c * a

    return f


print("Testes:")

for i in range(len(teste_x)):

    x1 = teste_x[i]
    y1 = teste_y[i]

    print(f"x = {x1}, y = {y1}, sqrt(x^2 + y^2) = {moler(x1, y1)}")


# Calcular norma do de um vertor de dimensão n

n = int(input("\nDimensao do vetor: "))
v = []

for i in range(n):
    v.append(float(input(f"{i + 1}a coordenada: ")))

f = moler(v[0], v[1])

for i in range(n - 2):
    f = moler(f, v[i + 2])

print(f"norma do vetor: {f}")
