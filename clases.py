import random

# ------------------------------    CLASE DETECTOR   ------------------------------


class Detector:
    def __init__(self, adn: list, repeticiones: int = 4) -> None:
        self.adn = adn
        self.repeticiones = repeticiones
        self.mutacion_horizontal = False
        self.mutacion_vertical = False
        self.mutacion_diagonal = False

    def existe_mutacion(self, linea: str) -> bool:
        """
        existe_mutación método que recibe un string como argumento y devuelve un booleano
        Detecta repeticiones consecutivas de un mismo caracter en una cadena.
        Si hay 4 repeticiones consecutivas del mismo caracter en la cadena dada devuelve True
        Caso contrario devuelve False
        """
        for i in range(len(linea) - 3):
            if linea[i] == linea[i + 1] == linea[i + 2] == linea[i + 3]:
                return True
        return False

    def detectar_mutantes(self, adn: list) -> bool:
        """
        Método encargado de detectar si hay una mutación horizontal, vertical o diagonal en el ADN que recibe como argumento.
        Devuelve un booleano (True si se encuentra alguna mutación, False si no hay mutaciones)
        """
        self.mutacion_horizontal = self.detectar_horizontal(adn)
        self.mutacion_vertical = self.detectar_vertical(adn)
        self.mutacion_diagonal = self.detectar_diagonal(adn)

        return (
            self.mutacion_horizontal or self.mutacion_vertical or self.mutacion_diagonal
        )

    def detectar_horizontal(self, adn: list) -> bool:
        """
        detectar_horizontal método que recibe una matriz de ADN como argumento y devuelve un booleano,
        recorre las filas de la matriz y hace uso del método existe_mutación para corroborar si hay una repetición de al menos 4 caracteres consecutivos
        """
        for linea in adn:
            if self.existe_mutacion(linea):
                return True
        return False

    def detectar_vertical(self, adn: list) -> bool:
        """
        detectar_vertical método que recibe una matriz de ADN como argumento y devuelve un booleano,
        recorre las filas de la matriz y genera un string concatenando la primera letra de cada fila para formar la columna.
        Hace uso del método existe_mutación para corroborar si hay una repetición de al menos 4 caracteres consecutivos
        """
        for i in range(len(adn[0])):
            columna = "".join(fila[i] for fila in adn)
            if self.existe_mutacion(columna):
                return True
        return False

    def detectar_diagonal(self, adn: list) -> bool:
        """
        detectar_diagonal método que recibe una matriz de ADN como argumento y devuelve un booleano,
        recorre las filas y columnas, creando un string con los caracteres que forman las diagonales, en ambos sentidos, de la matriz en las que pueda haber 4 caracteres repetidos consecutivamente.
        Hace uso del método existe_mutación para corroborar si hay una repetición de al menos 4 caracteres consecutivos
        """
        limite = len(adn)

        for i in range(limite - 3):
            # diagonales que comienzan en la fila 0 columna 0, desplazándose hacia la derecha
            diagonal_1 = "".join(adn[j][i + j] for j in range(limite - i))

            # diagonales que comienzan en la fila 0 columna 0 desplazándose hacia abajo
            diagonal_2 = "".join(adn[i + j][j] for j in range(limite - i))
            if self.existe_mutacion(diagonal_1) or self.existe_mutacion(diagonal_2):
                return True

        for i in range(limite - 3):
            # Diagonales que comienzan en la fila 0 columna n, desplazándose hacia la izquierda
            diagonal_3 = "".join(adn[j][limite - 1 - i - j] for j in range(limite - i))

            # Diagonales que comienzan en la fila 0 columna n, desplazándose hacia abajo
            diagonal_4 = "".join(adn[i + j][limite - 1 - j] for j in range(limite - i))
            if self.existe_mutacion(diagonal_3) or self.existe_mutacion(diagonal_4):
                return True

        return False


# ------------------------------    CLASE MUTADOR   ------------------------------


class Mutador:
    def __init__(
        self, adn: list, base_nitrogenada: str, posicion_inicial: tuple = [0, 0]
    ) -> None:
        self.adn = adn
        self.base_nitrogenada = base_nitrogenada
        self.posicion_inicial = posicion_inicial

    def crear_mutante(self):
        """
        Método vacío llamado crear_mutante
        """
        pass


# ------------------------------    CLASE RADIACIÓN   ------------------------------


class Radiacion(Mutador):
    def __init__(
        self,
        adn: list,
        base_nitrogenada: str,
        orientacion_de_la_mutacion: str,
        posicion_inicial: tuple = ...,
    ) -> None:
        super().__init__(adn, base_nitrogenada, posicion_inicial)
        self.orientacion_de_la_mutacion = orientacion_de_la_mutacion

    def crear_mutante(
        self,
        base_nitrogenada: str,
        posicion_inicial: tuple,
        orientacion_de_la_mutacion: str,
    ) -> list:
        """
        método crear_mutante
        Recibe como argumentos:
        - base_nitrogenada
        - posicion_inicial: tupla con valores numéricos para determinar la posición inicial de la mutación en filas y columnas
        - orientacion_de_la_mutacion cuyos posibles valores son: "V" (vertical) / "H" (horizontal)
        Haciendo uso de manejo de errores a través de los bloques try/except el método llama a las funciones crear_mutacion_horizontal o
        crear_mutacion_vertical dependiendo del valor del argumento orientacion_de_la_mutacion y devuelve la matriz modificada
        """
        mutacion = [
            base_nitrogenada
        ] * 4  # crea una lista a insertar con la repetición de la base_nitrogenada
        fila_inicial = posicion_inicial[0]  # posición inicial en filas
        col_inicial = posicion_inicial[1]  # posicion inicial en columnas

        try:
            if orientacion_de_la_mutacion not in ["H", "V"]:
                raise ValueError(
                    "La orientacion de la mutación deve ser V (vertical) u H (horizontal)"
                )
            if orientacion_de_la_mutacion == "H":
                self.adn = self.crear_mutacion_horizontal(
                    self.adn, mutacion, fila_inicial, col_inicial
                )
            elif orientacion_de_la_mutacion == "V":
                self.adn = self.crear_mutacion_vertical(
                    self.adn, mutacion, fila_inicial, col_inicial
                )
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")
        return self.adn

    def crear_mutacion_horizontal(
        self, adn: list, mutacion: list, fila: int, col: int
    ) -> list:
        """
        método crear_mutacion_horizontal
        recibe como argumentos:
        - adn: La matriz de adn a modificar
        - mutacion: una lista con la base_nitrogenada repetida 4 veces a insertar dentro de la matriz
        - fila y col: enteros que delimitan la posición inicial dónde insertar la mutación
        El método verifica que la posición inicial más el largo de la mutación no exceda el largo de la matriz en columnas, inserta la mutación y devuelve la matriz adn modificada
        caso contrario, arroja un error y devuelve la matriz recibida, sin modificar
        """

        try:
            if (col + len(mutacion)) <= len(adn[0]):
                for i in range(len(mutacion)):
                    adn[fila][col + i] = mutacion[i]
            else:
                raise IndexError("No se puede insertar la mutación en la posición dada")
        except IndexError:
            print("No se puede insertar la mutación en la posición dada")
        except Exception as e:
            print(e)
        finally:
            return adn

    def crear_mutacion_vertical(
        self, adn: list, mutacion: list, fila: int, col: int
    ) -> list:
        """
        método crear_mutacion_vertical
        recibe como argumentos:
        - adn: La matriz de adn a modificar
        - mutacion: una lista con la base_nitrogenada repetida 4 veces a insertar dentro de la matriz
        - fila y col: enteros que delimitan la posición inicial dónde insertar la mutación
        El método verifica que la posición inicial más el largo de la mutación no exceda el largo de la matriz en filas e inserta la mutación y devuelve la matriz adn modificada
        caso contrario, arroja un error y devuelve la matriz recibida, sin modificar
        """
        try:
            if (fila + len(mutacion)) <= len(adn[0]):
                for i in range(len(mutacion)):
                    adn[fila + i][col] = mutacion[i]
            else:
                raise IndexError("No se puede insertar la mutación en la posición dada")
        except IndexError as ie:
            print(f"Error: {ie}")
        except Exception as e:
            print(e)
        finally:
            return adn


# ------------------------------    CLASE VIRUS   ------------------------------


class Virus(Mutador):
    def __init__(
        self,
        adn: list,
        base_nitrogenada: str,
        posicion_inicial: int,
        orientacion_de_la_mutacion="D",
    ) -> None:
        super().__init__(adn, base_nitrogenada, posicion_inicial)
        self.orientacion_de_la_mutacion = orientacion_de_la_mutacion

    def crear_mutante(
        self, adn: list, base_nitrogenada: str, posicion_inicial: tuple
    ) -> list:
        """
        método crear_mutante
        recibe como argumentos:
        - adn: la matriz de adn a modificar
        - base_nitrogenada: el valor de la base nitrogenada que va a mutar el adn
        - posicion_inicial: tupla con valores numéricos para determinar la posición inicial de la mutación en filas y columnas
        Haciendo uso de manejo de errores a través de los bloques try/except el método genera una lista repitiendo 4 veces la base_nitrogenada
        y determina si la posición inicial en filas y columnas más el largo de la mutación no excede el largo de la matriz.
        En ese caso, inserta la mutación en la diagonal deseada, devolviendo la matriz modificada.
        Caso contrario, devuelve la matriz sin modificar.
        """
        mutacion = [base_nitrogenada] * 4
        fila = posicion_inicial[0]
        columna = posicion_inicial[1]

        try:
            if (fila + len(mutacion) <= len(adn[0])) and (
                columna + len(mutacion) <= len(adn[0])
            ):
                for i in range(len(mutacion)):
                    adn[fila + i][columna + i] = mutacion[i]
            else:
                raise IndexError("No se puede insertar la mutación en la posición dada")
        except IndexError as ie:
            print(f"Error: {ie}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            return adn


# ------------------------------    CLASE SANADOR   ------------------------------


class Sanador:
    def __init__(self, adn: list) -> None:
        self.adn = adn
        self.detector = Detector(adn=None)
        self.bases_nitrogenadas = ["A", "T", "C", "G"]

    def es_mutante(self, adn: list) -> bool:
        """
        método es_mutante
        recibe como argumento una lista de adn y devuelve un booleano
        Utiliza una instancia de la clase detector para acceder al método detectar_mutantes
        Devuelve True si en el adn que recibe existe alguna mutación y False en caso contrario
        """
        return self.detector.detectar_mutantes(adn)

    def sanar_mutantes(self, adn: list) -> list:
        """
        método sanar_mutantes:
        Método encargado de sanar cualquier tipo de mutación. Recibe como argumento una matris de ADN.
        Por medio de un bucle while verifica si el adn recibio contiene una mutación o no
        En caso de existir una mutación llama al método generar_adn() y vuelve a verificar que la nueva matriz no contenga mutaciones
        Devuelve una nueva matriz de ADN sin mutaciones
        """
        while self.es_mutante(adn):
            self.adn = self.generar_adn()
            if self.es_mutante(self.adn) == False:
                return self.adn
        return adn

    def generar_adn(self) -> list:
        """
        método generar_adn
        Método que genera una nueva matriz de ADN
        """
        n_filas = len(self.adn)
        n_cols = len(self.adn)
        nuevo_adn = []

        for i in range(n_filas):
            fila_adn = "".join(
                random.choice(self.bases_nitrogenadas) for j in range(n_cols)
            )
            nuevo_adn.append(fila_adn)

        return nuevo_adn
