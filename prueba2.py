# para solicitar el numero de puntos a interpolar
num_puntos = int(input('Ingrese el número de puntos a interpolar: '))

# creando las listas para almacenar los valores que el usuario va a ingresar ya transformado en los valores de la matriz
X = []
Y = []

# pidiendo al usuario que ingrese las coordenadas de los puntos a interpolar
for i in range(num_puntos):
    x = float(input(f'Ingrese el valor de la coordenada x_{i+1}: '))
    y = float(input(f'Ingrese el valor de la coordenada x_{i+1}: '))
    
    # guardando las filas para la matriz de la forma polinomica
    X.append([x**j for j in range(num_puntos)]) 
    Y.append(y)

# creando la funcion eliminacion gauss que acepta la matrix X y Y
def Eliminacion_gauss(X, Y):
    # obtenemos el numero de ecuaciones a resolver
    n= len(X)

    # Creando la matriz aumentada
    for i in range(n):
        
    
# resolver la matriz por eliminacion gauss
 
