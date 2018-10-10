from Sorts import MergeSort   #Se importa las funciones que se usaran
from Busquedas import InsertionSort
import sys						#Se utiliza para la leída de parámetros desde la terminal
import time 					#Se utiliza para "time"
import random 					#Genera números aleatorios

def Aleatorios(n):  			#Función que genera arreglo de tamaño n de números enteros aleatorios de -1000 a 1000
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(-1000, 1000)
      return lista

if int(sys.argv[2]) > 0 and (sys.argv[1] == "MergeSort" or sys.argv[1] == "InsertionSort"):  #Verifica si pone los parámetros correctos
	n = int(sys.argv[2])										#Lee el parámetro del usuario del tamaño de elementos del arreglo
	aleatorios=Aleatorios(n) 									#Llama a la funcion que genera el arreglo aleatorio
	if sys.argv[1] == "MergeSort": 								#Si es MergeSort. Calcula el tiempo que tarda en ordenarlo
		inicio = time.time()
		MergeSort(aleatorios,0,n-1)
		fin = time.time()
	else:
		if sys.argv[1] == "InsertionSort":  					#Si es InsertionSort. Calcula el tiempo que tarda en ordenarlo
			inicio = time.time()
			InsertionSort(aleatorios, 0, n)
			fin = time.time()
	print(f"Algoritmo: {sys.argv[1]}, numero de elementos: {sys.argv[2]} y tiempo empleado: {(fin-inicio) * 1000}")	
else:
	print("Entrada no válida")  				#Si no puso los parámetros correctamente, manda un mensaje de error y sale del programa