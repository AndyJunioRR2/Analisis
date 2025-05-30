def merge(A, p, q, r):
    nL = q - p + 1
    nR = r - q

    L = [0] * nL
    R = [0] * nR

    for i in range(nL):
        L[i] = A[p + i]
    for j in range(nR):
        R[j] = A[q + 1 + j]

    i = 0
    j = 0
    k = p

    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1

    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1

# Ejemplo de uso
A = [2, 5, 8, 1, 3, 7]
merge(A, 0, 2, 5)
print("Arreglo final:", A)


# Descripción del desarrollo
Entrada: Un arreglo A y tres índices p, q, r que definen dos subarreglos:

A[p : q] (subarreglo izquierdo)

A[q+1 : r] (subarreglo derecho)

Objetivo: Combinar (fusionar) estos dos subarreglos en un solo subarreglo ordenado dentro de A[p : r].

Pasos:

Se crean dos arreglos temporales L y R con los valores de cada mitad.

Se recorren ambos arreglos y se copian los elementos en orden al arreglo original A.

Si sobran elementos en L o R, se copian directamente.
 -Eficiencia del algoritmo
Tiempo: 
𝑂
(
𝑛
)
O(n), donde 
𝑛
=
𝑟
−
𝑝
+
1
n=r−p+1

Espacio: 
𝑂
(
𝑛
)
O(n) debido a los arreglos temporales L y R