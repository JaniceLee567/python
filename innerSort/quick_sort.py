#quick_sort:
#    description: confirm the priority, patch two parts; 
#    stability: unstable
#    time_complex:O(nlog2n) : O(nlog2n) : O(n^2)
import random

def quick_sort(array, low, high):
    print low, high
    if low < high:
        prior = depart(array, low, high)
        quick_sort(array, low, prior-1)
        quick_sort(array, prior+1, high)
#         print array

def depart(array, low, high):
    prior_key = array[low]
    while low < high:
        while(low < high and prior_key <= array[high]): # "=" important, otherwise, drop into endless loop
            high -= 1            
        array[low], array[high] = array[high], array[low]

        while(low < high and prior_key >= array[low]):
            low += 1
        array[low], array[high] = array[high], array[low]   
    
        
    print array    
    return low


if __name__ == '__main__':
    array = [random.randint(10, 50) for i in range(10)]
    print array
    quick_sort(array, 0, len(array)-1)
    print array