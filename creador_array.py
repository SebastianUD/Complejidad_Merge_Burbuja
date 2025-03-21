import random

def crear_array(n):
    array = []
    while len(array) < n:
        num = random.randint(1, n) 
        if num not in array:
            array.append(num)
    return array


