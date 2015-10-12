# shell_sort:
#	describtion:
#	stabilition: unstable
#	time_complex:

import random

def shell_sort(array):
	count = len(array)
	gap = count/2
	while(gap > 0):
		for i in range(0, gap):
			array_gap = [array[k] for k in range(i, count, gap)]
			print array_gap
			insert_sort(array_gap)
		print array
		gap = gap/2


def insert_sort(array):
	count = len(array)
	for i in range(1, count):
		key = array[i]
		for j in range(i-1, -1, -1):
			if array[j] > key:
				array[j+1] = array[j]
				k = j
			else:
				k = j+1
		array[k] = key
# 		print "insert_sort:", array

if __name__ == '__main__':
	array = [random.randint(10, 50) for i in range(6)]
	print array
	shell_sort(array)
