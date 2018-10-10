# Busquedas.py
# Autor: Ivette C. Martínez
# Modificado por: 
# Descripcion: Implementacion de los algoritmos de busqueda lineal y BusquedaBinaria

def LecturaDeDatos (arreglo):  #Funcion que carga el arreglo de un archivo
	w=open(arreglo,"rt")
	O=[]
	for i in w:
		O.append(i)
	m=O[0].split()    
	m=[int(i) for i in O]    
	w.close()
	return m

def Ordenan(arreglo):		#Funcion que verifica si un arreglo esta ordenado
	t=0
	while t  < len(arreglo):
		if arreglo[t] <= arreglo[t+1]:
			pass
		else:
			return False
		t += 1
		break

	return True

def BusquedaLineal(arreglo, x):		#Funcion de Busqueda Lineal

	for i in range(len(arreglo)):
		if arreglo[i] == x:
			return i
	return None 

def BusquedaBinaria(arreglo, x):	#Funcion de Busqueda Binaria
	
	start = 0					#Se establece las posiciones de inicio y final del arreglo
	end = len(arreglo)
	# 
	while start < end:
		mid = (start+end) // 2	#Division entera
		if arreglo[start] == x:	#Se busca si esta en la posicion inicial
			return start
		else:
			if arreglo[mid] == x:	#Se busca si esta en el medio 
				return mid
			else:
				if arreglo[mid] < x:	#No esta en arreglo[start...mid]
					start = mid + 1
				else:					#No esta en arreglo[mid...end]
					end = mid - 1

	return None 

def InsertionSort(A, p, r):	#Funcion de Ordenamiento por Insercion
	for j in range(p+1,r):
		llave = A[j]			#Elemento a insertar
		#Pone al elemento en la posicion correcta
		i = j - 1
		while i >= p and A[i] > llave:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = llave
	return A