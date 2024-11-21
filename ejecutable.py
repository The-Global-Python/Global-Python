""" 
Código que pida al usuario que ingrese un ADN y pregunte si desea detectar mutaciones, mutarlo o sanarlo. 
Dependiendo de la respuesta, se deben instanciar las clases necesarias y devolver el ADN final junto con algún mensaje informando 
al respecto del computo realizado.
"""

from clases import Detector, Radiacion, Virus, Sanador


def cargar_nuevo_adn(largo: int = 6) -> list:
    print("El ADN debe contener 6 cadenas con 6 caracteres (A, C, G, T)")
    nuevo_adn = []
    while len(nuevo_adn) < largo:
        fila = input(f"Ingrese la cadena {len(nuevo_adn) + 1}: ").upper()
        if validar_cadena(fila):
            nuevo_adn.append(fila)
        else:
            print("Cadena inválida: Debe contener 6 caracteres y solo A, C, G, T")
    return nuevo_adn


def validar_cadena(fila: str) -> bool:
    bases_nitrogenadas = ["A", "C", "G", "T"]
    if len(fila) == 6:
        validados = list(filter(lambda char: char in bases_nitrogenadas, fila))
        if len(validados) == 6:
            return True
    return False


def detectar_mutaciones(adn: list) -> None:
    detector = Detector(adn)
    if detector.detectar_mutantes(adn):
        print("El ADN es mutante")
    else:
        print("El ADN no es mutante")


def seleccionar_mutacion(adn: list) -> int:
    while True:
        try:
            mutacion = int(input("Seleccione una opción: "))
            print("--------------------------------------")
            if mutacion == 1:
                return mutacion
            elif mutacion == 2:
                return mutacion
            else:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 2")
        except ValueError:
            print("Error: la opción ingresada no es válida")


def mutacion_con_radiacion(adn: list) -> list:
    adn_matriz = [list(fila) for fila in adn]

    while True:
        try:
            base_nitrogenada = input(
                "Ingrese la base nitrogenada a repetir (A, T, C, G): "
            ).upper()
            if base_nitrogenada not in ["A", "T", "C", "G"]:
                raise ValueError("La base nitrogenada debe ser A, T, C, o G.")
            else:
                break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            fila_inicial = int(input("Ingrese la posicion inicial en filas: "))
            if not (0 <= fila_inicial < len(adn_matriz)):
                raise ValueError(
                    f"Fila fuera de rango. Debe estar entre 0 y {len(adn_matriz) - 1}"
                )
            else:
                break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            columna_inicial = int(input("Ingrese la posicion inicial en columnas: "))
            if not (0 <= columna_inicial < len(adn_matriz[0])):
                raise ValueError(
                    f"Columna fuera de rango. Debe estar entre 0 y {len(adn_matriz[0]-1)}"
                )
            else:
                break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            orientacion_de_la_mutacion = input(
                "Ingrese la orientacion de la mutación: Horizontal(H) / Vertical(V): "
            ).upper()
            if orientacion_de_la_mutacion not in ["H", "V"]:
                raise ValueError(
                    "La orientacion debe ser 'H' para horizontal o 'V' para vertical"
                )
            else:
                break
        except ValueError as e:
            print(f"Error: {e}")

    radiacion = Radiacion(
        adn_matriz,
        base_nitrogenada,
        orientacion_de_la_mutacion,
        [fila_inicial, columna_inicial],
    )
    matriz_mutada = radiacion.crear_mutante(
        base_nitrogenada, [fila_inicial, columna_inicial], orientacion_de_la_mutacion
    )
    print("-------------------- ADN MUTADO --------------------")
    for i in matriz_mutada:
        print(i)
    print("----------------------------------------------------")
    return matriz_mutada


def mutacion_con_virus(adn: list) -> list:
    adn_matriz = [list(fila) for fila in adn]
    while True:
        try:
            base_nitrogenada = input(
                "Ingrese la base nitrogenada a repetir (A, T, C, G): "
            ).upper()
            if base_nitrogenada not in ["A", "T", "C", "G"]:
                raise ValueError("La base nitrogenada debe ser A, T, C, o G.")
            else:
                break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            fila_inicial = int(input("Ingrese la posicion inicial en filas: "))
            if not (0 <= fila_inicial < len(adn_matriz)):
                raise ValueError(
                    f"Fila fuera de rango. Debe estar entre 0 y {len(adn_matriz) - 1}"
                )
            else:
                break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            columna_inicial = int(input("Ingrese la posicion inicial en columnas: "))
            if not (0 <= columna_inicial < len(adn_matriz[0])):
                raise ValueError(
                    f"Columna fuera de rango. Debe estar entre 0 y {len(adn_matriz[0]-1)}"
                )
            else:
                break
        except ValueError as e:
            print(f"Error: {e}")

    virus = Virus(adn_matriz, base_nitrogenada, [fila_inicial, columna_inicial])
    matriz_mutada = virus.crear_mutante(
        adn_matriz, base_nitrogenada, [fila_inicial, columna_inicial]
    )
    print("-------------------- ADN MUTADO --------------------")
    for i in matriz_mutada:
        print(i)
    print("----------------------------------------------------")
    return matriz_mutada


def sanar_adn_mutante(adn: list) -> list:
    sanador = Sanador(adn)
    adn_sanado = sanador.sanar_mutantes(adn)
    print("-------------------- ADN SANADO --------------------")
    for i in [list(fila) for fila in adn_sanado]:
        print(i)
    print("----------------------------------------------------")
    return adn_sanado


def mostrar_adn(adn: list) -> None:
    adn_matriz = [list(fila) for fila in adn]
    for i in adn_matriz:
        print(i)


def main() -> None:
    print("Crear una matriz de ADN")
    adn = cargar_nuevo_adn()
    acciones = []
    while True:
        print("--------------------------------------")
        print("¿Qué desea hacer con el ADN?")
        print("1) Detectar mutaciones")
        print("2) Mutar el ADN")
        print("3) Sanar el ADN")
        print("4) Mostrar el ADN")
        print("5) Salir")
        try:
            seleccion = int(input("Seleccione una opción: "))
            print("--------------------------------------")
            if seleccion == 1:
                detectar_mutaciones(adn)
                acciones.append("DETECCIÓN")
            elif seleccion == 2:
                print("¿Qué tipo de mutación desea crear?")
                print("1) Radiación (horizontal o vertical)")
                print("2) Virus (diagonal)")
                tipo_mutacion = seleccionar_mutacion(adn)
                if tipo_mutacion == 1:
                    adn = mutacion_con_radiacion(adn)
                    acciones.append("MUTACIÓN CON RADIACION")
                elif tipo_mutacion == 2:
                    adn = mutacion_con_virus(adn)
                    acciones.append("MUTACIÓN CON VIRUS")
            elif seleccion == 3:
                adn = sanar_adn_mutante(adn)
                acciones.append("SANACIÓN")
            elif seleccion == 4:
                mostrar_adn(adn) 
                acciones.append("MUESTRA")
            elif seleccion == 5:
                print("--------------- ACCIONES REALIZADAS ----------------")
                for i in acciones:
                    print(i)
                print("------------------ ADN RESULTADO -------------------")
                mostrar_adn(adn)
                print("----------------------------------------------------")
                break
            else:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 4")
        except ValueError:
            print("Error: debe ingresar un número válido")


if __name__ == "__main__":
    main()
