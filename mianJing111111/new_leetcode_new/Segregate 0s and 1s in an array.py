# encoding=utf-8
'''

Segregate 0s and 1s in an array

Asked by kapil.

You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array. Traverse array only once.

Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

Method 1 (Count 0s or 1s)
Thanks to Naveen for suggesting this method.
1) Count the number of 0s. Let count be C.
2) Once we have count, we can put C 0s at the beginning and 1s at the remaining n – C positions in array.
数数的方法。 很好！ two pass
Time Complexity: O(n)

The method 1 traverses the array two times. Method 2 does the same in a single pass.


2个指针。  one pass
Method 2 (Use two indexes to traverse)
Maintain two indexes. Initialize first index left as 0 and second index right as n-1.

Do following while left < right
a) Keep incrementing index left while there are 0s at it
b) Keep decrementing index right while there are 1s at it
c) If left < right then exchange arr[left] and arr[right]


这是sort  color   leetcode的简化版

特点是只有0， 1
如果是把0移到后面去。 有很多其他元素。 用2个指针。 fast, slow. 也是one pass

'''

class Solution:
    def segregate0and1(self, arr):
        l=0; r = len(arr)-1
        while l<r:
            while l<r and arr[l]==0 :  l+=1
            while l<r and arr[r]==1 :  r-=1
            arr[l], arr[r] = arr[r], arr[l]  #交换
            l+=1;  r-=1
