import time # Importar la libreria time

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
# Caso de prueba 1
start = time.time() # Iniciar el tiempo
print(busqueda_linea([1, 2, 3, 4, 5], 3)) # 2
end = time.time() # Finalizar el tiempo
# imprimir el tiempo de ejecucion
print(f"Tiempo de ejecucion: {end - start:.10} segundos") # Imprimir el tiempo de ejecucion

# Caso de prueba 2
start = time.time() # Iniciar el tiempo
print(busqueda_linea([1, 2, 3, 4, 5], 6)) # -1
end = time.time() # Finalizar el tiempo
print(f"Tiempo de ejecucion: {end - start:.10} segundos") # Imprimir el tiempo de ejecucion

# Caso de prueba 3
start = time.time() # Iniciar el tiempo
print(busqueda_linea([1, 2, 3, 4, 5], 1)) # 0
end = time.time() # Finalizar el tiempo
print(f"Tiempo de ejecucion: {end - start:.10} segundos") # Imprimir el tiempo de ejecucion
