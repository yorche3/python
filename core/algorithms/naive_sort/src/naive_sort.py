# naive_sort — ordenamientos elementales O(n²).
#
# Especificación: 05_Naive_Sort
#
# Contrato: recibe una lista de enteros y devuelve la lista ordenada de menor a
# mayor (in-place o como copia ordenada), sin invocar bibliotecas de
# ordenamiento del sistema ni estructuras auxiliares complejas.
# Si la entrada es None devuelve None como indicador de fallo; si está vacía
# devuelve la misma lista vacía. No lanza excepciones.
#
# Implementación pendiente: la escribe el autor. Esta delegación solo genera el
# esqueleto y las pruebas unitarias.
def selection_sort(arr):
    if arr is None:
        return None
    n = len(arr)
    if n < 2:
        return arr
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    if arr is None:
        return None
    n = len(arr)
    if n < 2:
        return arr
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    if arr is None:
        return None
    n = len(arr)
    if n < 2:
        return arr
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr