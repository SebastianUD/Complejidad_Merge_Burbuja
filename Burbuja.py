import Random_Array
from Random_Array import crear_array

array = crear_array() # Crear un array aleatorio
pasos = 0 # Contador de pasos
for i in range(len(array)):
    for j in range(len(array)-1):
        if array[i] < array[j]:
            aux = array[i]
            array[i] = array[j]
            array[j] = aux
        pasos += 1
    pasos += 1

print("Array ordenado: ")
print(array)
print(f"Los pasos esperados segun la formula (fn = n^2) son: {(len(array))**2}")
print(f"Los pasos totales del codigo fueron {pasos}")