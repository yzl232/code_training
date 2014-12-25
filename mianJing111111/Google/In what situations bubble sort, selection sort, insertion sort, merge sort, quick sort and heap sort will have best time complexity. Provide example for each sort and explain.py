# encoding=utf-8
'''
In what situations bubble sort, selection sort, insertion sort, merge sort, quick sort and heap sort will have best time complexity. Provide example for each sort and explain
'''

'''
Selection Sort : Best Worst Average Case running time all O(n^2). However the number of swaps required is always n-1. Hence it is useful when the amount of satellite data(auxiliary data aside from the key) is large and for some reason pointer based swapping is not feasible.

Insertion Sort : Best case running time is O(n). Hence useful for adding new data to a presorted list. Also this is fast when the number of elements is small/ you need an online algorithm.

Bubble Sort:Where we know the data is very nearly sorted. Say only two elements are out of place. Then in one pass, BS will finish it and in the second pass, it will see everything is sorted and then exit. Only takes 2 passes of the array.

Merge Sort : For external sorting algorithms, it is the choice of sort.

Quicksort : Remember that quicksort is dependent on choice of pivot. So when we have absolutely random data values, and we will need to sort them, we have to use quick sort. Even for very unbalanced split QS produces good results.

Heap Sort: It is an inplace O(n logn) algorithm hence we can use it when we cannot afford the extra space required for merge sort. Also has a O(n logn) worst case time as compared to O(n^2) of quicksort.
'''


'''
Bubble/insertion/merge sorts are stable.
Selection/quick/heap sorts are not stable.

Quicksort:
Also, I don't understand your "we have to use quicksort" comment.
For very unbalanced splits QS produces good results ... you should explain this better. Also, no mention of the fact that QS isn't often used in hard real time systems if the worst case (n^2) can't be tolerated for some inputs.
Also, the usual implementation of quicksort (subroutine partition) does too many swaps when there are duplicate keys. So often quicksort is avoided when the data will have a lot of repeated keys.
'''