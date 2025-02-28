# Matriz 3x3
matriz = [
    [21, 22, 23],
    [26, 25, 24],
    [27, 28, 29]
]
# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                if not swapped: break

def print_matrix(matriz):
    for row in matriz:
        print(row)

print("Matriz original:")
print_matrix(matriz)

# Ordenar la fila específica

fila_a_ordenar = 1

bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz con la fila ordenada:")
print_matrix(matriz)
