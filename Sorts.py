# Sorts.py
def MergeSort(A, p, r):
	if p < r :
		q = (p+r)//2 		#División entera para hallar la mitad de A
		MergeSort(A,p,q)	#MergeSort de la primera mitad
		MergeSort(A,q+1,r)	#MergeSort de la segunda mitad
		Merge(A,p,q,r)		#Merge de las dos partes del arreglo 
	return A		

def Merge(A, p, q, r):
	L = A[p:q+1]			#Creamos un arreglo L que contiene la primera mitad de A
	R = A[q+1:r+1]			#Creamos un arreglo L que contiene la segunda mitad de A
							#Centinelas de L y R
	L.append(float('inf'))
	R.append(float('inf'))

	i = j = 0
	for k in range(p,r+1):	#Se comparan los elementos de los arreglos L y R y se ordena de menor a mayor el arreglo A
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1	
	return A