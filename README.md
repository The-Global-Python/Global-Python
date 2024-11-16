# Proyecto de Detección y Mutación de ADN

## Descripción
Este proyecto tiene como objetivo detectar, mutar y sanar secuencias de ADN. El programa permite al usuario ingresar una matriz de ADN de 6x6 y realizar diferentes operaciones sobre ella, como detectar mutaciones, crear mutaciones mediante radiación o virus, y sanar el ADN mutado.

## Participantes
- Leandro Azcurra
- Lisandro Romero
- Octavio Skumanic

## Instrucciones de Ejecución

1. Clona el repositorio en tu máquina local:
    ```sh
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```

2. Navega al directorio del proyecto:
    ```sh
    cd tu-repositorio
    ```

3. Ejecuta el programa principal:
    ```sh
    python main.py
    ```

## Ejemplo de Uso

### Ingreso del ADN
El programa solicitará que ingreses el ADN en forma de una matriz de 6x6. Por ejemplo:

ATGCGA
CAGTGC
TTATGT
AGAAGG
CCCCTA
TCACTG
### Opciones del Menú
El programa presentará un menú con las siguientes opciones:
1. Detectar mutaciones
2. Mutar el ADN
3. Sanar el ADN

### Ejemplo de Detección de Mutaciones
Si seleccionas la opción 1, el programa detectará si el ADN es un mutante o no.

**Input:** 1
**Output:** El ADN es un mutante


### Ejemplo de Mutación del ADN
Si seleccionas la opción 2, el programa te permitirá crear una mutación mediante radiación o virus.

### Mutación de ADN
**Output:**
  ¿Qué desea hacer?
    1. Detectar mutaciones
    2. Mutar el ADN
    3. Sanar el ADN
    Seleccione una opción (1/2/3):
**Input:** 2
Esto selecciona la opción de mutar el ADN.

**Output:**
¿Qué tipo de mutación desea crear?
	1. Radiación (horizontal o vertical)
	2. Virus (diagonal)

**Input:** 1
Esto selecciona la opción de mutación por radiación.

**Output:**
Ingrese la base nitrogenada a repetir (A, T, C, G):

**Input:** A
Esto especifica que la base nitrogenada a repetir es 'A'.

**Output:**
Ingrese la posición inicial (fila, columna):

**Input:** 0 0
Esto indica la posición inicial (fila 0, columna 0) donde comenzará la mutación.

**Output:**
Ingrese la orientación de la mutación (H para horizontal, V para vertical):

**Input:** H
Esto indica que la orientación de la mutación es horizontal.

**Output:**
ADN mutado:
AAAAAA
CAGTGC
TTATGT
AGAAGG
CCCCTA
TCACTG


### Ejemplo de Sanación del ADN
Si seleccionas la opción 3, el programa sanará el ADN mutado generando una nueva matriz de ADN.

**Input:** 3

**Output:**

**Output:**
ADN sanado:
GTACGA
CAGTGC
TTATGT
AGAAGG
CCCCTA
TCACTG
## Notas
- Asegúrate de ingresar las filas de la matriz de ADN correctamente, cada fila debe tener exactamente 6 caracteres.
- Las opciones de mutación y sanación modificarán la matriz de ADN original.
