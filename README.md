# **Proyecto de Detección y Mutación de ADN**

Este proyecto es una aplicación interactiva para gestionar matrices de ADN. Permite detectar mutaciones, realizar mutaciones de diferentes tipos y sanar ADN mutante. Está diseñado para analizar secuencias de bases nitrogenadas (`A`, `C`, `G`, `T`) y realizar modificaciones siguiendo reglas predefinidas.

---

## **Integrantes**

- Leandro Azcurra
- Leandro Mercado
- Lisandro Romero
- Octavio Skumanic

---
## **Características**

### 1. **Detección de Mutaciones**
   - Verifica si el ADN ingresado tiene mutaciones horizontales, verticales o diagonales.
   - Las mutaciones se definen como repeticiones consecutivas de 4 bases nitrogenadas iguales en la matriz.

### 2. **Mutaciones**
   - **Radiación:** Crea mutaciones horizontales o verticales en la matriz de ADN.
   - **Virus:** Genera mutaciones diagonales en la matriz de ADN.

### 3. **Sanación de ADN**
   - Identifica y reemplaza ADN mutado con una nueva matriz generada aleatoriamente hasta eliminar todas las mutaciones.

### 4. **Interfaz Interactiva**
   - Permite al usuario:
     - Cargar una nueva matriz de ADN.
     - Detectar mutaciones.
     - Crear mutaciones personalizadas.
     - Sanar el ADN.
     - Mostrar el estado actual del ADN.

---

## **Ejecución**

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/gestion-adn.git
   cd gestion-adn
   ```

2. Ejecuta el programa principal:
   ```bash
   python main.py
   ```

3. Sigue las instrucciones en pantalla para interactuar con el programa.

---

## **Uso**

### Carga de ADN
- Se solicita al usuario ingresar 6 cadenas de 6 caracteres cada una (`A`, `C`, `G`, `T`).
- Ejemplo de entrada válida:
  ```
  ATGCGA
  CAGTGC
  TTATGT
  AGAAGG
  CCCCTA
  TCACTG
  ```

### Opciones del Menú
1. **Detectar Mutaciones:**
   - Muestra si el ADN tiene mutaciones y de qué tipo (horizontal, vertical o diagonal).

2. **Mutar el ADN:**
   - Selecciona entre:
     - Radiación: Inserta mutaciones horizontales o verticales en una posición específica.
     - Virus: Inserta mutaciones diagonales.

3. **Sanar el ADN:**
   - Genera una nueva matriz hasta eliminar todas las mutaciones.

4. **Mostrar el ADN:**
   - Visualiza la matriz actual del ADN.

5. **Salir:**
   - Termina la ejecución del programa.

---

## **Ejemplo de Flujo**

1. **Cargar ADN inicial:**
   - Entrada:
     ```
     ATGCGA
     CAGTGC
     TTATGT
     AGAAGG
     CCCCTA
     TCACTG
     ```
   - Salida:
     ```
     ADN cargado con éxito.
     ```

2. **Detectar Mutaciones:**
   - Salida:
     ```
     El ADN es mutante. Mutación detectada: Horizontal.
     ```

3. **Mutar ADN:**
   - Selecciona **Radiación**:
     - Base nitrogenada: `A`
     - Posición inicial: (2, 1)
     - Orientación: Horizontal
   - Salida:
     ```
     ADN mutado con éxito.
     ```

4. **Sanar ADN:**
   - Salida:
     ```
     ADN sanado. No se encontraron mutaciones.
     ```

5. **Mostrar ADN:**
   - Salida:
     ```
     ['A', 'T', 'G', 'C', 'G', 'A']
     ['C', 'A', 'G', 'T', 'G', 'C']
     ...
     ```


