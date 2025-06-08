import pandas as pd
import timeit

# Cargamos el dataset
df = pd.read_csv("paraphrased_all_ASAG.csv")

# Buscamos algun valor que se encuentre repetido en el dataset, para usar como ejemplo
valores_frecuencia = df['student_answer_paraphrased'].value_counts()
valor_objetivo = valores_frecuencia.index[0]

# Convertimos los valores a una lista para ejecutar las busquedas
data_list = df['student_answer_paraphrased'].tolist()
sorted_list = sorted(data_list)

# Definimos los metodos de busqueda

def busqueda_lineal(data, objetivo):
  for i, val in enumerate(data):
    if val == objetivo:
      return i
  return -1

def busqueda_binaria(data, objetivo):
  izq, der = 0, len(data) - 1
  while izq <= der:
      med = (izq + der) // 2
      if data[med] == objetivo:
          return med
      elif data[med] < objetivo:
          izq = med + 1
      else:
          der = med - 1
  return -1

# Medimos el tiempo de cada metodo

tiempo_lineal = timeit.timeit(lambda: busqueda_lineal(data_list, valor_objetivo), number = 100)

tiempo_binario = timeit.timeit(lambda: busqueda_binaria(sorted_list, valor_objetivo), number=100)

# En el caso de busqueda binaria, tenemos que considerar el tiempo que toma ordenar la lista
tiempo_ordenamiento = timeit.timeit(lambda: sorted(data_list), number=100)

tiempo_binario_total = tiempo_binario + tiempo_ordenamiento

# Imprimo resultados

print(f"Valor objetivo: {repr(valor_objetivo)}")
print(f"Tiempo de busqueda lineal: {tiempo_lineal:.6f} segundos")
print(f"Tiempo de busqueda binaria: {tiempo_binario:.6f} segundos")
print(f"Tiempo de ordenamiento: {tiempo_ordenamiento:.6f} segundos")
print(f"Total tiempo binario + tiempo de ordenamiento: {tiempo_binario_total:.6f} segundos")

import matplotlib.pyplot as plt

labels = ['Búsqueda Lineal', 'Búsqueda Binaria', 'Ordenamiento', 'Búsq. Binaria + Ord.']

tiempos = [tiempo_lineal, tiempo_binario, tiempo_ordenamiento, tiempo_binario_total]

# Se crea un gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(labels, tiempos)

plt.ylabel('Tiempo (segundos)')
plt.title('Comparando algoritmos de búsqueda en Python')
plt.grid(axis='y')

plt.tight_layout()

plt.show()
