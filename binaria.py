import timeit

edades = [34, 21, 45, 19, 60, 27, 38, 22, 15, 8]

""" Función de ordenamiento por selección """


def ordenar_edades(lista):
    n = len(lista)
    for i in range(n):
        pos_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i], lista[pos_menor] = lista[pos_menor], lista[i]


""" Función de búsqueda binaria """


def busqueda_binaria(lista, valor):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1


ordenar_edades(edades)
print("Edades ordenadas: ", edades)

valor_buscar = int(input("Que edad queres buscar? "))


""" Tiempo de busqueda """

inicio = timeit.default_timer()
resultado = busqueda_binaria(edades, valor_buscar)
fin = timeit.default_timer()


""" Mostrar resultado """

if resultado != -1:
    print(f"El valor {valor_buscar} fue encontrado en la posición {resultado}")

    print("Tiempo de busqueda:", fin - inicio, "segundos")

else:
    print(f"El valor {valor_buscar} no se encuentra en la lista")

    print("Tiempo de busqueda:", fin - inicio, "segundos")
