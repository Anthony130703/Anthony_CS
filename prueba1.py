# Función de eliminación gaussiana
def gauss_elimination(X, Y):
    n = len(X)

    # Crear la matriz aumentada (agregar el vector Y a la matriz X)
    for i in range(n):
        X[i].append(Y[i])

    # Paso 1: Transformación de la matriz a forma triangular superior
    for i in range(n):
        # Hacer el pivote (el valor X[i][i] debe ser diferente de 0)
        if X[i][i] == 0:
            for j in range(i+1, n):
                if X[j][i] != 0:
                    X[i], X[j] = X[j], X[i]
                    break

        # Hacer ceros debajo de X[i][i]
        for j in range(i+1, n):
            ratio = X[j][i] / X[i][i]
            for k in range(i, n+1):
                X[j][k] -= ratio * X[i][k]

    # Paso 2: Sustitución hacia atrás para encontrar los coeficientes
    solution = [0] * n
    for i in range(n-1, -1, -1):
        sum_ = 0
        for j in range(i+1, n):
            sum_ += X[i][j] * solution[j]
        solution[i] = (X[i][n] - sum_) / X[i][i]

    return solution

# Solicitar al usuario cuántos puntos ingresará
num_puntos = int(input("¿Cuántos puntos vas a ingresar? "))

# Inicializar matrices X y Y
X = []
Y = []

# Pedir al usuario los puntos
for i in range(num_puntos):
    x = float(input(f"Ingrese el valor de x_{i+1}: "))
    y = float(input(f"Ingrese el valor de y_{i+1}: "))
    # Crear una fila para la matriz X con los monomios [1, x, x^2, ..., x^(n-1)]
    X.append([x**j for j in range(num_puntos)])  # Monomios hasta x^(n-1)
    Y.append(y)

# Resolver el sistema usando eliminación gaussiana
coeficientes = gauss_elimination(X, Y)

# Mostrar el polinomio resultante
polinomio = "P(x) = "
for i, coef in enumerate(coeficientes):
    if coef >= 0:
        polinomio += f"+ {coef:.2f}x^{i} " if i > 0 else f"{coef:.2f} "
    else:
        polinomio += f"- {abs(coef):.2f}x^{i} " if i > 0 else f"- {abs(coef):.2f} "

print(polinomio)
