import time # Importar la libreria time

def busqueda_binaria(list, valor):
    # Inicializar los valores de los indices
    inicio = 0
    fin = len(list) - 1
    # Mientras el inicio sea menor o igual al fin
    while inicio <= fin:
        # Calcular el medio
        medio = (inicio + fin) // 2
        # Si el valor es igual al valor del medio
        if list[medio] == valor:
            # Retornar el medio
            return medio
        # Si el valor es mayor al valor del medio
        elif list[medio] < valor:
            # Mover el inicio al medio + 1
            inicio = medio + 1
        # Si el valor es menor al valor del medio
        else:
            # Mover el fin al medio - 1
            fin = medio - 1
    # Si no se encontro el valor
    return -1

# Casos de pruebas
# Caso de prueba 1
start = time.time() # Iniciar el tiempo
print(busqueda_binaria([1, 2, 3, 4, 5], 3)) # 2
end = time.time() # Finalizar el tiempo
print(f"Tiempo de ejecucion: {end - start:.10} segundos") # Imprimir el tiempo de ejecucion

# Caso de prueba 2
start = time.time() # Iniciar el tiempo
print(busqueda_binaria([1, 2, 3, 4, 5], 6)) # -1
end = time.time() # Finalizar el tiempo
print(f"Tiempo de ejecucion: {end - start:.10} segundos") # Imprimir el tiempo de ejecucion

# Caso de prueba 3
start = time.time() # Iniciar el tiempo
print(busqueda_binaria([1, 2, 3, 4, 5], 1)) # 0
end = time.time() # Finalizar el tiempo
print(f"Tiempo de ejecucion: {end - start:.10} segundos") # Imprimir el tiempo de ejecucion