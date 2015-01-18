# encoding=utf-8
#简单做法是用hash
'''

Check if array elements are consecutive | Added Method 3

Given an unsorted array of numbers, write a function that returns true if array consists of consecutive numbers.

Examples:
a) If array is {5, 2, 3, 1, 4}, then the function should return true because the array has consecutive numbers from 1 to 5.

b) If array is {83, 78, 80, 81, 79, 82}, then the function should return true because the array has consecutive numbers from 78 to 83.

c) If the array is {34, 23, 52, 12, 3 }, then the function should return false because the elements are not consecutive.

d) If the array is {7, 6, 5, 5, 3, 4}, then the function should return false because 5 and 5 are not consecutive.

'''

#方法一'
'''
O(n) space

1) max – min + 1 = n where max is the maximum element in array, min is minimum element in array and n is the number of elements in array.
2) All elements are distinct.
'''
class Solution:
    def find(self, arr):
        return max(arr)-min(arr)+1==len(arr) == len(set(arr))   # set实质是hashtable。用了 O(n) space

#方法2
'''
第一步一样。 第二步：it changes the original array and it works only if all numbers are positive.

arr[arr[i] - min]] as a negative value. If we see a negative value again then there is repetition.
'''
# Find duplicates in O(n) time and O(1) extra space

#inplace
class Solution3:  #假定没有负数出现
    def isCon(self, arr):  #利用index, 以及正负标记. 来check是否重复
        small = min(arr)
        if max(arr)-small+1!=len(arr): return False  #注意，置为负数时候，必须为arr[i]-minVal
        for i in range(len(arr)):
            t = abs(arr[i])-small  #因为max-min = length。  所以abs(arr[i])-small一定OK
            if arr[t]<0: return False
            else: arr[t]=-arr[t]
        return True