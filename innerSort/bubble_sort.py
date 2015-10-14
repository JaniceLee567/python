#bubble_sort:
#	description: the former and latter number is changed all the time. 
#                only the maximum number occurred in the last position
#	stability: unstable
#	time_complex: O(n^2), the best is O(n)

import random

def bubble_sort(array):
    account = len(array)
    for i in range(account-1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp

        print array


if __name__ == '__main__':
    array = [random.randint(10, 50) for i in range(10)]
    print array
    bubble_sort(array)
