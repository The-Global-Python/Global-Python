import random

class Detector:
    def __init__(self, matriz):
        self.matriz = matriz

    def detectar_mutantes(self):
        return (self.verificar_filas() or
                self.verificar_columnas() or
                self.verificar_diagonales_izq_der() or
                self.verificar_diagonales_der_izq())

    def verificar_filas(self):
        for fila in self.matriz:
            if self.verificar_secuencia(fila):
                return True
        return False

    def verificar_columnas(self):
        for col in range(6):
            columna = [self.matriz[i][col] for i in range(6)]
            if self.verificar_secuencia(columna):
                return True
        return False

    def verificar_diagonales_izq_der(self):
        for i in range(3):
            for j in range(3):
                diagonal = [self.matriz[i+k][j+k] for k in range(4)]
                if self.verificar_secuencia(diagonal):
                    return True
        return False

    def verificar_diagonales_der_izq(self):
        for i in range(3):
            for j in range(3, 6):
                diagonal = [self.matriz[i+k][j-k] for k in range(4)]
                if self.verificar_secuencia(diagonal):
                    return True
        return False

    def verificar_secuencia(self, secuencia):
        for i in range(len(secuencia) - 3):
            if secuencia[i] == secuencia[i+1] == secuencia[i+2] == secuencia[i+3]:
                return True
        return False

class Mutador:
    def __init__(self, base_nitrogenada, atributo1, atributo2):
        self.base_nitrogenada = base_nitrogenada
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def crear_mutante(self):
        pass

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, atributo1, atributo2):
        super().__init__(base_nitrogenada, atributo1, atributo2)

    def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        try:
            if orientacion_de_la_mutacion == "H":
                for i in range(4):
                    matriz[posicion_inicial[0]][posicion_inicial[1] + i] = base_nitrogenada
            elif orientacion_de_la_mutacion == "V":
                for i in range(4):
                    matriz[posicion_inicial[0] + i][posicion_inicial[1]] = base_nitrogenada
            else:
                raise ValueError("Orientación no válida")
            return matriz
        except Exception as e:
            print(f"Error al crear mutante: {e}")
            return matriz

class Virus(Mutador):
    def __init__(self, base_nitrogenada, atributo1, atributo2):
        super().__init__(base_nitrogenada, atributo1, atributo2)

    def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial):
        try:
            for i in range(4):
                matriz[posicion_inicial[0] + i][posicion_inicial[1] + i] = base_nitrogenada
            return matriz
        except Exception as e:
            print(f"Error al crear mutante: {e}")
            return matriz

class Sanador:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def sanar_mutantes(self, matriz):
        detector = Detector(matriz)
        if detector.detectar_mutantes():
            nueva_matriz = self.generar_nueva_matriz()
            return nueva_matriz
        return matriz

    def generar_nueva_matriz(self):
        bases = ['A', 'T', 'C', 'G']
        nueva_matriz = []
        for _ in range(6):
            fila = ''.join(random.choices(bases, k=6))
            nueva_matriz.append(fila)
        return nueva_matriz