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
        ret= [1 ]*(len(arr))
        left=ret[:]; right = ret[:]
        for i in range(1, len(arr)):
            left[i] = left[i-1] * arr[i-1]   #都是i-1。 不大一样。
        for i in range(len(arr)-2, -1, -1):
            right[i] = right[i+1]*arr[i+1]
        for i in range(len(arr)):
            ret[i] = left[i] * right[i]
        return ret

#有 not extra space 的做法
class Solution3:
    def product(self, arr):
        cur=1; ret =[1]*len(arr)
        for i in range(len(arr)):
            ret[i]*=cur
            cur *=arr[i]  # cur放在后面
        cur = 1
        for i in range(len(arr)-1, -1, -1):
            ret[i]*=cur
            cur *=arr[i]
        return ret
s = Solution3()
print s.product([2,3,1,4])

# G家考过类似的。 求和版本
'''
You are given an array of integers 'a' that can fit in a memory. Write a method that retuns an array of the same lenght such that each element 'i' of this array is a sum of 'a' except the element a[i]. You are not allowed to use '-' operator.
'''
class Solution3:
    def product(self, arr):
        cur=0; ret =[0]*len(arr)
        for i in range(len(arr)):
            ret[i]+=cur
            cur +=arr[i]
        cur = 0
        for i in range(len(arr)-1, -1, -1):
            ret[i]+=cur
            cur +=arr[i]
        return ret