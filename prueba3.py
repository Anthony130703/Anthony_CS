#! /usr/bin/python3
from numpy import *
import matplotlib.pyplot as plt # from pylab import plot,show
import warnings
warnings.filterwarnings("ignore")

# Cargar datos
datos = loadtxt("data1.txt", float)
Q = datos[:, 0]
N = datos[:, 1]
n = len(Q)

# Construir matriz X y vector Y
X = [[Q[i]**j for j in range(n)] for i in range(n)]
Y = list(N)

# Función de eliminación gaussiana
def gauss_elimination(X, Y):
    n = len(X)
    for i in range(n):
        X[i].append(Y[i])
    for i in range(n):
        if X[i][i] == 0:
            for j in range(i+1, n):
                if X[j][i] != 0:
                    X[i], X[j] = X[j], X[i]
                    break
        for j in range(i+1, n):
            ratio = X[j][i] / X[i][i]
            for k in range(i, n+1):
                X[j][k] -= ratio * X[i][k]
    solution = [0] * n
    for i in range(n-1, -1, -1):
        sum_ = sum(X[i][j] * solution[j] for j in range(i+1, n))
        solution[i] = (X[i][n] - sum_) / X[i][i]
    return solution

# Obtener coeficientes
coef = gauss_elimination([fila[:] for fila in X], Y)

# Mostrar el polinomio
polinomio = "N(Q) = "
for i, c in enumerate(coef):
    if c >= 0:
        polinomio += f"+ {c:.6f}*Q^{i} " if i > 0 else f"{c:.6f} "
    else:
        polinomio += f"- {abs(c):.6f}*Q^{i} " if i > 0 else f"- {abs(c):.6f} "
print(polinomio)

# Graficar
import numpy as np
Q_vals = np.linspace(min(Q), max(Q), 400)
N_vals = sum(c * Q_vals**i for i, c in enumerate(coef))

plt.figure(figsize=(10, 6))
plt.plot(Q, N, 'ro', label='Datos')
plt.plot(Q_vals, N_vals, 'b-', label='Polinomio interpolado')
plt.xlabel("Q (l/h)")
plt.ylabel("N (w)")
plt.title("Interpolación polinómica por eliminación gaussiana")
plt.legend()
plt.grid(True)
plt.show()
