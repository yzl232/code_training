# encoding=utf-8
'''
input [2,3,1,4]
output [12,8,24,6]

Multiply all fields except it's own position.

Restrictions:
1. no use of division
2. complexity in O(n)

#如果能用除法就好了。  直接求所有乘积，再除以。


Maintain two arrays - front [ ] and rear [ ]
front maintains the product before the current index
rear maintains the product after the current index
then the product of current index i = front[i]*rear[i]


arr = 2, 3, 1, 4

// maintain two arrays which can be done in O(n)

arr1 = 2,  6,   6,  24 (arrays multiply each number with previous and current)
arr2 = 24, 12, 4, 4    (arrays multiplied from end)

In above two arrays, put 1 in beginning of arr1 and end of arr2:
arr1 = 1, 2,  6,   6,  24, 1
arr2 = 24, 12, 4, 4,   1

Then to find number at index 'i' you would just do:

arr1[i]*arr2[i+1]

i之前的乘积
i之后的乘积    都不包括i

'''
class Solution:
    def specialProduct(self, arr):
        result = left = right = [1 for i in range(len(arr))]
        for i in range(1, len(arr)):
            left[i] = left[i-1] * arr[i-1]
        for i in range(len(arr)-2, -1, -1):
            right[i] = right[i+1]*arr[i+1]
        for i in range(len(arr)):
            result[i] = left[i] * right[i]
        return result

#有O(1),  one pass的算法