# Programa para la gestión y reserva de asientos en una sala de cine 

def gestionar_reserva_cine():
    # 1. Creación e inicialización de la matriz (3 filas x 4 columnas) con ceros (asiento libre)
    asientos = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    print("--- SISTEMA DE RESERVA DE CINE ---")

    # 2. Solicitar fila y columna al usuario validando los rangos permitidos (0 a 2 para filas, 0 a 3 para columnas)
    while True:
        try:
            fila = int(input("Ingrese la fila que desea reservar (0 a 2): "))
            columna = int(input("Ingrese la columna que desea reservar (0 a 3): "))

            # Verificación de rango válido
            if 0 <= fila <= 2 and 0 <= columna <= 3:
                break
            else:
                print("Error: La fila debe estar entre 0 y 2, y la columna entre 0 y 3. Intente nuevamente.\n")
        except ValueError:
            print("Error: Debe ingresar números enteros válidos.\n")

    # 3. Marcar el asiento seleccionado como reservado (valor 1)
    asientos[fila][columna] = 1
    print(f"\n¡Éxito! El asiento en la fila {fila}, columna {columna} ha sido reservado.\n")

    # 4. Mostrar la matriz completa en formato de tabla usando bucles anidados
    print("Estado actual de la sala (0 = Libre, 1 = Reservado):")
    for i in range(len(asientos)):  # Recorrido de filas (0 a 2)
        for j in range(len(asientos[i])):  # Recorrido de columnas (0 a 3)
            print(asientos[i][j], end=" ")  # Imprime los valores en la misma línea
        print()  # Salto de línea al finalizar cada fila


if __name__ == "__main__":
    gestionar_reserva_cine()