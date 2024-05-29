def busqueda_linea(list, valor):
    # Posicion del valor en la lista
    posicion = 0
    # Recorrer la lista
    for i in list:
        # Si el valor es igual al valor de la lista
        if i == valor:
            # Retornar la posicion
            return posicion
        # Aumentar la posicion
        posicion += 1
    # Si no se encontro el valor
    return -1


# Casos de pruebas
print(busqueda_linea([1, 2, 3, 4, 5], 3)) # 2
print(busqueda_linea([1, 2, 3, 4, 5], 6)) # -1
print(busqueda_linea([1, 2, 3, 4, 5], 1)) # 0
