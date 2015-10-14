# shell_sort:
#	description: cut array with gap, and each patch use insert_sort
#	stability: unstable
#	time_complex: can not to ensure

import random

def shell_sort(array):
	count = len(array)
	gap = count/2
	while(gap > 0):
		for i in range(0, gap):
			insert_sort(array, i, count, gap)
			print "gap=", gap, "array=", array
		print array
		gap = gap/2


def insert_sort(array, i, count, gap):
	count = len(array)
	for m in range(i+gap, count, gap):
		key = array[m]
		for j in range(m-gap, -1, -gap):
			if array[j] > key:
				array[j+gap] = array[j]
				k = j
			else:
				k = j+gap
				break
		array[k] = key
# 		print "insert_sort:", array

if __name__ == '__main__':
	array = [random.randint(10, 50) for i in range(10)]
	print array
	shell_sort(array)
# 	insert_sort(array, 0, 10, 2)
