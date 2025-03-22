import Random_Array as array

# Importar la función para crear un array aleatorio
array.crear_array()

pasos = 0  # Contador de pasos

def merge_sort(arr):
    global pasos
    
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        pasos += 1  # Contar la división en dos subarreglos
        
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Mezclar los subarreglos L y R en arr
        while i < len(L) and j < len(R):
            pasos += 1  # Contar la comparación
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            pasos += 1  # Contar la asignación en arr[k]

        # Copiar los elementos restantes de L, si los hay
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            pasos += 1  # Contar cada asignación

        # Copiar los elementos restantes de R, si los hay
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            pasos += 1  # Contar cada asignación

# Ejecutar el algoritmo
merge_sort(array.array)

# Imprimir los resultados
print("\nArray ordenado:")
print(array.array)

print("\nNúmero total de pasos:", pasos/2)