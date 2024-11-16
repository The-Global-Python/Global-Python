from clases import Detector, Radiacion, Virus, Sanador

def main():
    matriz = []
    print("Ingrese el ADN (6 filas de 6 caracteres cada una):")
    for _ in range(6):
        fila = input()
        matriz.append(fila)

    print("¿Qué desea hacer?")
    print("1. Detectar mutaciones")
    print("2. Mutar el ADN")
    print("3. Sanar el ADN")
    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == '1':
        detector = Detector(matriz)
        if detector.detectar_mutantes():
            print("El ADN es un mutante")
        else:
            print("El ADN no es un mutante")

    elif opcion == '2':
        print("¿Qué tipo de mutación desea crear?")
        print("1. Radiación (horizontal o vertical)")
        print("2. Virus (diagonal)")
        tipo_mutacion = input("Seleccione una opción (1/2): ")

        if tipo_mutacion == '1':
            base_nitrogenada = input("Ingrese la base nitrogenada a repetir (A, T, C, G): ")
            posicion_inicial = tuple(map(int, input("Ingrese la posición inicial (fila columna): ").split()))
            orientacion_de_la_mutacion = input("Ingrese la orientación de la mutación (H para horizontal, V para vertical): ")
            radiacion = Radiacion(base_nitrogenada, None, None)
            matriz_mutada = radiacion.crear_mutante(matriz, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion)
            print("ADN mutado:")
            for fila in matriz_mutada:
                print(fila)

        elif tipo_mutacion == '2':
            base_nitrogenada = input("Ingrese la base nitrogenada a repetir (A, T, C, G): ")
            posicion_inicial = tuple(map(int, input("Ingrese la posición inicial (fila columna): ").split()))
            virus = Virus(base_nitrogenada, None, None)
            matriz_mutada = virus.crear_mutante(matriz, base_nitrogenada, posicion_inicial)
            print("ADN mutado:")
            for fila in matriz_mutada:
                print(fila)

    elif opcion == '3':
        sanador = Sanador(None, None)
        matriz_sanada = sanador.sanar_mutantes(matriz)
        print("ADN sanado:")
        for fila in matriz_sanada:
            print(fila)

    else:
        print("Opción no válida")


main()