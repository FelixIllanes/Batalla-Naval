import random

# Batalla Naval

 
# El Tablero

# Cada tablero contiene una cuadrícula 10 x 10. El eje horizontal está 
# rotulado con letras de la A a la J, y de forma vertical la numeración del 1 al 10.

# Condiciones  

# Coordenadas: Acción para elegir una casilla con letra y con número.
# Casilla vacía : Es la representación en el tablero del agua
# Tiro acertado: Se menciona la coordenada correcta, significa que impactamos en su nave 
# y se debe marcar por pantalla, Si es  "Hundido" si todos los casilleros del barco han sido ya impactados. Se pondrá un marcador rojo.
# Barcos: Cada jugador tendrá 5 barcos, un portaaviones (cinco casillas), un acorazado (cuatro casillas), un crucero (tres casillas), un submarino (tres casillas) y un destructor (dos casillas).

 
# Reglas

# Cada jugador tiene un turno
# Gana el juego cuando todos los barcos son hundidos
# No se considera empate


FILAS = 10
COLUMNAS = 10
MAR = " "
PORTA_AVIONES = "P" # Ocupa 5 espacios
ACORAZADO = "A"     # Ocupa 4 espacios
CRUCERO = "C"       # Ocupa 3 espacios
SUBMARINO = "S"     # Ocupa 3 espacios
DESTRUCTOR = "D"    # Ocupa 2 espacios
DISPARO_FALLADO = "0"    # Cuando se falle un disparo se asignara 0 a la coordenada
DISPARO_ACERTADO = "X"   # Cuando se acierte un disparo se asignara x a la coordenada
CANTIDAD_BARCOS_INICIALES = 5
JUGADOR_1 = "J1"
JUGADOR_2 = "J2"


# Función para crear el tablero inicialmente vacio
def tablero_inicial():
    matriz = []
    for y in range(FILAS):
        matriz.append([])
        for x in range(COLUMNAS):
            matriz[y].append(MAR)
    return matriz

# Funcion para generar las letras de (A - J)
def incrementar_letra(letra):
    return chr(ord(letra)+1)


def separador_horizontal():
    for _ in range(COLUMNAS+1):
        print("+---", end="")
    print("+")


def fila_de_numeros():
    print("|   ", end="")
    for x in range(COLUMNAS):
        print(f"| {x+1} ", end="")
    print("|")


# Indica si una coordenada de la matriz está vacía
def es_mar(x, y, matriz):
    return matriz[y][x] == MAR

# Verifica que la coordenada se encuentre dentro del rango del tablero
def en_rango(x, y):
    return x >= 0 and x <= COLUMNAS-1 and y >= 0 and y <= FILAS-1

# Ubica de manera aleatoria los barcos en el tablero
def ingresar_barcos(matriz, cantidad_barcos, jugador):

    if jugador == JUGADOR_1:
        print("Barcos del Jugador 1 ")
    else:
        print("Barcos del Jugador 2 ")
    
    # Ingresamos cada tipo de barco, iniciando por el que ocupa mas espacios 
    matriz = colocar_barcos_vertical(1, PORTA_AVIONES, matriz, 5)

    matriz = colocar_barcos_vertical(1, ACORAZADO, matriz, 4)
    
    matriz = colocar_barcos_horizontal(1, CRUCERO, matriz, 3)

    matriz = colocar_barcos_horizontal(1, SUBMARINO, matriz, 3)
    
    matriz = colocar_barcos_horizontal(1, DESTRUCTOR, matriz, 2)
    

    return matriz

# Funciones para obtener las coordenadas aleatorias
def obtener_x_aleatoria():
    return random.randint(0, COLUMNAS-1)


def obtener_y_aleatoria():
    return random.randint(0, FILAS-1)

# Funciones para validar si la coordenada esta dentro del tablero y si los espacios
# necesarios para ingresar el barco estan vacios
def validar_y(x,y,matriz, tamaño):
    aux = 1
    resp = True
    while aux <= tamaño:
        if en_rango(x,y) and es_mar(x,y,matriz):
            y += 1
            aux += 1
        else:
            return False
    return resp

def validar_x(x,y,matriz, tamaño):
    aux = 1
    resp = True
    while aux <= tamaño:
        if en_rango(x,y) and es_mar(x,y,matriz):
            x += 1
            aux += 1
        else:
            return False
    return resp
    

# Funciones para ingresar los barcos en la matriz
def colocar_barcos_vertical(cantidad, tipo_barco, matriz,tamaño):
    barcos_colocados = 0
    bandera = True
    bandera2 = True
    aux2 = 1
    x = 0
    y = 0
    
    while bandera2:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()

        if validar_y(x,y,matriz, tamaño):
            bandera2 = False
    
    while bandera:
        if aux2 <= tamaño: 
            matriz[y][x] = tipo_barco
            y = y + 1
            aux2 = aux2 + 1
        else:
            barcos_colocados += 1  
               
        if barcos_colocados == cantidad:
            bandera = False
    return matriz

def colocar_barcos_horizontal(cantidad, tipo_barco, matriz,tamaño):
    barcos_colocados = 0
    bandera = True
    bandera2 = True
    aux2 = 1
    x = 0
    y = 0

    while bandera2:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()

        if validar_x(x,y,matriz, tamaño):
            bandera2 = False

    while bandera:
        if aux2 <= tamaño: 
            matriz[y][x] = tipo_barco
            x = x + 1
            aux2 = aux2 + 1
        else:
            barcos_colocados += 1  
                
        if barcos_colocados == cantidad:
            bandera = False
    return matriz


# Funcion para formar e imprimir el tablero
def imprimir_matriz(matriz, deberia_mostrar_barcos, jugador):
    print(f"Este es el tablero del Jugador {jugador}: ")
    letra = "A"
    separador_horizontal()
    fila_de_numeros()
    for y in range(FILAS):
        separador_horizontal()
        print(f"| {letra} ", end="")
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            valor_real = celda
            if not deberia_mostrar_barcos and valor_real != MAR and valor_real != DISPARO_FALLADO and valor_real != DISPARO_ACERTADO:
                valor_real = " "
            print(f"| {valor_real} ", end="")
        letra = incrementar_letra(letra)
        print("|",)  # Salto de línea
    separador_horizontal()


def solicitar_coordenadas(jugador):
    print(f"Solicitando coordenadas de disparo al jugador {jugador}")
    # Ciclo infinito. Se rompe cuando ingresan una fila correcta
    y = None
    x = None
    while True:
        letra_fila = input(
            "Ingresa la letra de la fila en mayusculas: ")
        # Validaciones para fila, se debe ingresar solo un caracter
        if len(letra_fila) != 1:
            print("Debes ingresar únicamente una letra")
            continue
        # Convertimos la letra a un indice para acceder a matriz utilizando ASCII
        y = ord(letra_fila) - 65
        # Verificar si es válida. En caso de que sí, salimos del ciclo
        if en_rango(0, y):
            break
        else:
            print("Fila inválida")
    # Validaciones para columna
    while True:
        try:
            x = int(input("Ingresa el número de columna: "))
            if en_rango(x-1, 0):
                x = x-1  # Restamos 1 para obtener el indice
                break
            else:
                print("Columna inválida")
        except:
            print("Ingresa un número válido")

    return x, y

# Función para verficar si se acerto o fallo el disparo 
def disparar(x, y, matriz):
    if es_mar(x, y, matriz):
        matriz[y][x] = DISPARO_FALLADO
        return False
    # Se cuenta como falla si vuelve a disparar a las mismas coordenadas
    elif matriz[y][x] == DISPARO_FALLADO or matriz[y][x] == DISPARO_ACERTADO:
        return False
    else:
        matriz[y][x] = DISPARO_ACERTADO
        return True

# Funcion para cambiar de turno
def oponente_de_jugador(jugador):
    if jugador == JUGADOR_1:
        return JUGADOR_2
    else:
        return JUGADOR_1

# Para definir si aun hay barcos en el tablero o si ya se derribaron todos
def todos_los_barcos_hundidos(matriz):
    for y in range(FILAS):
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            # Verificamos si hay celdas diferentes a vacio, agua o disparo acertado
            # en caso de que si exista alguna entonces aun hay un barco 
            if celda != MAR and celda != DISPARO_ACERTADO and celda != DISPARO_FALLADO:
                return False

    return True


def indicar_victoria(jugador):
    print(f"Fin del juego\nEl jugador {jugador} es el ganador")

# Imprime las coordenadas donde se disparo y donde se encontraban los barcos de cada jugador
def imprimir_matrices_con_barcos(matriz_j1, matriz_j2):
    print("Mostrando ubicación de los barcos de ambos jugadores:")
    imprimir_matriz(matriz_j1, True, JUGADOR_1)
    imprimir_matriz(matriz_j2, True, JUGADOR_2)

# Funcion para iniciar la Batalla Naval
def jugar():
    cantidad_barcos = 5
    # Creación de las dos matrices para los jugadores, inicialmente vacias
    matriz_j1, matriz_j2 = tablero_inicial(), tablero_inicial()
    
    # Rellenamos ambas matrices con los barcos en posiciones aleatorias
    matriz_j1 = ingresar_barcos(matriz_j1, cantidad_barcos, JUGADOR_1)
    matriz_j2 = ingresar_barcos(matriz_j2, cantidad_barcos, JUGADOR_2)
    
    turno_actual = JUGADOR_1
    print("===============")
                   
    while True:
        # Iniciamos con el jugador J1
        print(f"Turno de {turno_actual}")
        matriz_oponente = matriz_j1

        if turno_actual == JUGADOR_1:
            matriz_oponente = matriz_j2
        # Si queremos ver las posiciones de los barcos cambiamos el False por un True
        # de esta manera podemos ver los barcos en el tablero del rival 
        # Caso contrario colocar False para que se escondan las posiciones de los barcos   
        imprimir_matriz(matriz_oponente, True, oponente_de_jugador(turno_actual))
        x, y = solicitar_coordenadas(turno_actual)
        acertado = disparar(x, y, matriz_oponente)

        imprimir_matriz(matriz_oponente, True, oponente_de_jugador(turno_actual))
        
        # Verificamos si el disparo fue acertado y tambien si aun quedan barcos en el
        # tablero rival
        if acertado:
            print("Disparo acertado")
            if todos_los_barcos_hundidos(matriz_oponente):
                indicar_victoria(turno_actual)
                imprimir_matrices_con_barcos(matriz_j1, matriz_j2)
                break
        else:
            print("Disparo fallado")
        # Cambio de turno
        turno_actual = oponente_de_jugador(turno_actual) 


jugar()