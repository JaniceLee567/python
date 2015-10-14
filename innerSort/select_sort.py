#simple_select_sort:
#	description: each time, select the max/min number 
#		      and change with the first number.
#		      each time, only one number's position is changed.
#	stability: unstable
#	time_complex: O(n^2)

import random

def select_sort(array):
	account = len(array)
	for i in range(0, account-1):
		min = i
		for j in range(i, account): 
			if array[min] > array[j]:
				min = j  # reverse, select the index of minNumber
		if min != i:
			tmp = array[i]
			array[i] = array[min]
			array[min] = tmp

		print array


if __name__ == '__main__':
	array = [random.randint(10, 50) for i in range(10)]
	select_sort(array)
