import random

# Variable Global
array = []

def crear_array():
    # Preguntar al usuario el rango de números
    print("Seleccione el rango de números aleatorios a ordenar:")
    print("1. Del 1 al 100")
    print("2. Del 1 al 1000")
    print("3. Del 1 al 10000")
    print("4. Si desea introducir un numero especifico")
    
    opcion = int(input("\nIngrese su opción (1, 2, 3 o 4): "))
    
    match opcion:
        case 1:
            n = 100
        case 2:
            n = 1000
        case 3:
            n = 10000
        case 4:
            n = int(input("Introduzca el número: "))
        case _:
            print("Opción no válida. Se usará el rango del 1 al 100 por defecto.")
            n = 100
    
    # Mostrar el array desordenado
    print("\nArray generado aleatoriamente sin ordenamiento:")
    while len(array) < n:
        num = random.randint(1, n) 
        if num not in array:
            array.append(num)
    print(array)
    
    # Devolver el array anteriormente creado para usarse en los diferentes algoritmos
    return array