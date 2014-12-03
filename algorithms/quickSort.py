import random  
  
L = [2, 3, 8, 4, 9, 5, 6, 5, 6, 10, 17, 11, 2]  
  
def quickSort(L):
    if len(L) <=1: return L
    pivot = random.choice(L)
    small = [i for i in L if i < pivot]
    middle = [ i for i in L if i== pivot]
    big = [i for i in L if i>pivot]
    return quickSort(small) + middle + quickSort(big)

print quickSort(L)



#quick selection  O(n)
def quickSelect(a, k):
    pivot = random.choice(a)
    small = [i for i in a if i<pivot]
    middle = [i for i in a if i==pivot]     #写一下O(1)的partition写法。 这种效率略低。
    big = [i for i in a if i>pivot]
    s = len(small)
    m = len(middle)
    if s< k<=s+m:
        return pivot
    elif k<=s:
        return quickSelect(small, k)
    else:
        return quickSelect(big, k-m-s)



'''
以下是in place quick sort.  比较烦。 懒的搞
'''

def quicksort(array):
    _quicksort(array, 0, len(array) - 1)

def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)