# straight insert sort
#     assuming: before key, the occurrence is order
#     stability: stable
#     time_complex: O(n^2)

import random

def straight_insert_sort(array):
    count = len(array)

    for i in range(1, count):
        key = array[i]
        for j in range(i-1, -1, -1):
            if array[j] > key:
                array[j+1] = array[j]  # former larger and backward
                k = j   # reserve insert point
            else:
                k = j+1 # reserve insert point
                break  #*** important
        array[k] = key # insert data
        print array




if __name__ == '__main__':
    array = [random.randint(10, 50) for i in range(10)]
    print array
    straight_insert_sort(array) 
