# encoding=utf-8
'''
Implement a vector-like data structure from scratch.

Discussion topics:
1. Dealing with out of bounds accesses.
2. What happens when you need to increase the vector's size?
3. How many copies does the structure perform to insert n elements? That is, n calls to vector.push_back
'''

# logN

'''
Vector is implemented base on array, say size m.
1. If the array is full, create a new array of size 2m, copy the elements from original array to the new one, and put the to-be-inserted element into the new array
2. The size gets doubled.
3. If the array has size 0 for initialization, then you need log n copies to insert n elements.
'''