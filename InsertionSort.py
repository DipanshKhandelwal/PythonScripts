
import random 
import pylab
import numpy

def insertionSort(a):
	count = 0
	
	size = len(a)
	count+=1

	for i in range(1, size):
		count+=1
 
		key = a[i]
		count+=1

		j = i-1
		count+=1
		while j >= 0 and key < a[j] :
			count+=1
			count+=1
			count+=1
			a[j+1] = a[j]
			count+=1
			count+=1
			j = j - 1
			count+=1
			count+=1
		a[j+1] = key
		count+=1
		count+=1

	'''No need to return sorted array, just returning operation count'''
	return count;

def randomArray(n):

	a = []

	'''n will be between 3-16 and also generates random numbers within the range'''
	for i in range(1,n):
		a.append(random.randint(1,n))
	return a


'''main'''

dict = {}

''' For loop for 2^3 to 2^16'''
for i in range(3, 1):

	ops = 0
	i = 2**i

	dict[i] = 0

	'''running 5 times to take the average '''
	for j in range(1,6):
		
		count = insertionSort(randomArray(i))
		ops += count

	dict[i] = ops/5

for i in dict.items():

	print(i)












