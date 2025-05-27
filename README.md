# Semana 1 -  Algoritmia Elemental

## 1.1. Preliminares

### 1.1.1. Notación

La notación matemática permite expresar algoritmos de manera clara y estructurada.

- **Variables comunes**: `n`, `i`, `x`, etc.
- **Secuencias**: (a₁, a₂, ..., aₙ)
- **Sumatorias**:  
  Suma desde i = 1 hasta n de i:  
  ∑ i = 1 to n (i) = n(n + 1) / 2
- **Conjuntos numéricos**:
  - **N**: Números naturales
  - **Z**: Números enteros
  - **R**: Números reales

> **Importancia**: Facilita la comunicación matemática y el análisis formal de algoritmos.

---

### 1.1.2. Contradicción

Método lógico utilizado para demostrar que una proposición es verdadera.

- **Pasos**:
  1. Suponer que la afirmación es falsa.
  2. Derivar una contradicción lógica o matemática.
  3. Concluir que la afirmación original debe ser verdadera.

- **Ejemplo clásico**: demostrar que la raíz cuadrada de 2 (√2) es irracional.

> **Uso en algoritmos**: Comprobación de propiedades que deben cumplirse para que un algoritmo sea correcto.

---

### 1.1.3. Inducción matemática

Técnica para demostrar propiedades enunciadas sobre los números naturales.

- **Estructura**:
  1. **Paso base**: Verificar que la propiedad se cumple para n = 1.
  2. **Paso inductivo**: Suponer que se cumple para n = k y demostrar que también se cumple para n = k + 1.

- **Ejemplo**:
  Suma desde i = 1 hasta n de i:  
  ∑ i = 1 to n (i) = n(n + 1) / 2

> **Aplicación**: Comprobación de fórmulas, propiedades de algoritmos recursivos y comportamientos repetitivos.

---

### 1.1.4. Problemas

Sección dedicada a la aplicación de los conceptos teóricos mediante ejercicios.

- **Tipos de problemas**:
  - Secuencias y series numéricas
  - Pruebas por contradicción
  - Demostraciones por inducción
  - Análisis de estructuras recursivas

> **Objetivo**: Desarrollar el pensamiento lógico y aplicar herramientas matemáticas al diseño y análisis de algoritmos.
# Semana 2 – Algoritmia Elemental

## 1.2. Eficiencia de los algoritmos

La eficiencia de un algoritmo describe qué tan bien resuelve un problema en términos de recursos consumidos:

- **Tiempo de ejecución**: número de operaciones o pasos que realiza el algoritmo.
- **Uso de memoria**: cantidad de espacio que requiere durante su ejecución.

### Tipos de análisis:

- **Peor caso (Worst Case)**:
  - Describe el mayor número de pasos que puede requerir un algoritmo.
  - Se usa para garantizar un límite superior de tiempo.
  - Ejemplo: en una búsqueda lineal, si el elemento no está presente.

- **Mejor caso (Best Case)**:
  - Describe el menor número de pasos posibles.
  - Menos útil en práctica porque no refleja el comportamiento general.

- **Caso promedio (Average Case)**:
  - Mide el comportamiento esperado del algoritmo en entradas aleatorias.
  - Más realista pero a veces más difícil de calcular.

### Notaciones comunes:

- **O grande (Big O)**:  
  Representa un límite superior del tiempo de ejecución.  
  Ejemplo: O(n²), O(log n), O(n)

- **Ω (Omega)**:  
  Representa un límite inferior.

- **Θ (Theta)**:  
  Representa un ajuste exacto: tiempo en peor y mejor caso es el mismo orden.

> **Ejemplo de complejidades comunes**:
>
> - O(1): Tiempo constante  
> - O(log n): Tiempo logarítmico  
> - O(n): Tiempo lineal  
> - O(n log n): Tiempo casi lineal  
> - O(n²): Tiempo cuadrático  

---

## 1.3. Caso medio

El **análisis de caso medio** evalúa el comportamiento promedio del algoritmo, considerando todas las entradas posibles y su probabilidad de ocurrencia.

### Características:

- **Más representativo** que el mejor o peor caso.
- Puede requerir modelos probabilísticos para calcularlo.
- Útil para algoritmos como búsqueda binaria, ordenamientos o algoritmos aleatorizados.

> **Ejemplo**:  
> En búsqueda lineal de un arreglo de tamaño n, si el elemento a buscar está presente y todas las posiciones son igualmente probables, el número promedio de comparaciones es:  
> (1 + 2 + ... + n) / n = (n + 1) / 2

> **Importancia**: ayuda a entender cómo se comporta un algoritmo en condiciones normales, no extremas.
![Semana2](https://github.com/user-attachments/assets/5bb2ee05-67f6-4387-97f1-9d87d12c83f4)
# Semana 3 – Algoritmia Elemental

## 1.4. Caso peor

El **caso peor (Worst Case)** analiza la situación más desfavorable para un algoritmo, es decir, cuando tarda más en completarse.

### Características:

- Se utiliza para garantizar que un algoritmo no exceda cierto límite de tiempo.
- Proporciona una **cota superior** del tiempo de ejecución.
- Se expresa comúnmente con **notación Big O**: O(f(n))

> **Ejemplo**:  
> En búsqueda lineal, si el elemento no se encuentra, el algoritmo recorre todos los elementos.  
> Entonces el caso peor es O(n).

> **Importancia**:  
> Útil para diseñar algoritmos que deben responder rápidamente incluso en las peores condiciones.

---

## 1.5. Operación elemental

Una **operación elemental** es una acción básica e indivisible utilizada para medir el tiempo de ejecución de un algoritmo.

### Características:

- Tiene un costo constante (O(1))
- Depende del tipo de problema y del algoritmo.

### Ejemplos de operaciones elementales:

- Comparaciones (`==`, `<`, `>`)
- Asignaciones (`=`)
- Sumas, restas, multiplicaciones (dependiendo del contexto)
- Acceso a una posición de un arreglo (`A[i]`)

> **Importancia**:  
> Sirve como base para analizar cuántas operaciones realiza un algoritmo según el tamaño de entrada.

> **Ejemplo práctico**:  
> En un ciclo que recorre un arreglo de `n` elementos y realiza una comparación por iteración, se realizan `n` operaciones elementales (una por iteración).
# Semana 4 – Algoritmia Elemental

## 2. Notación asintótica

La notación asintótica es una forma de describir el comportamiento de un algoritmo cuando el tamaño de la entrada tiende a infinito.

- Permite comparar algoritmos sin depender de detalles específicos del hardware o implementación.
- Se enfoca en el crecimiento del tiempo o espacio requerido en función del tamaño del problema.

---

## 2.1. Notación para el "orden de"

Esta notación describe el crecimiento de la función que representa el tiempo de ejecución o uso de memoria.

### Notaciones principales:

- **Notación O grande (Big O):**  
  Representa un límite superior del crecimiento.  
  Ejemplo: O(n²) indica que el tiempo de ejecución crece a lo más proporcional a n².

- **Notación Ω (Omega):**  
  Límite inferior del crecimiento.

- **Notación Θ (Theta):**  
  Crecimiento exacto, es decir, límite superior e inferior iguales.

### Ejemplo:

Si un algoritmo realiza aproximadamente 3n² + 2n + 1 operaciones, su orden es:

- O(n²) porque los términos menores y constantes se ignoran en notación asintótica.

> **Uso práctico:**  
> Simplifica el análisis y la comparación de algoritmos, enfocándose en el factor dominante que afecta la eficiencia a gran escala.
![Semana4](https://github.com/user-attachments/assets/c9f3493a-d2de-4b20-86fc-1889a54d45f4)



