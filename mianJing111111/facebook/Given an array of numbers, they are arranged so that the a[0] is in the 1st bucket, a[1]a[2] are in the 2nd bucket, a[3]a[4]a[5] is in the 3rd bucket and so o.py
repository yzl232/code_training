# encoding=utf-8
'''

Given an array of numbers, they are arranged so that the a[0] is in the 1st bucket, a[1]a[2] are in the 2nd bucket, a[3]a[4]a[5] is in the 3rd bucket and so on.

All the numbers in one bucket are larger than that of the previous bucket.

So ALL numbers of bucket 3 will be bigger than ANY number of the bucket 2 and so on. The number given to the function may or may not be in the array.

The question is then: given a number, you need to return if it is in any bucket or not.
'''

#

'''



 in the m-th bucket, there are m element and in the (m+1)-th bucket, there are r elements where 1<=r<=m+1. So we have m(m+1)/2 + r = n. In O notation, we have m = O(sqrt(n)).



基本上就是binary search .     O( sqrt(N) +  logN)  = O( sqrt(N) ).   slightly better than brute force O(n)
'''
class Solution: #还是挺巧妙的。
    def find(self,arr, x):
        l=0; h=len(arr)
        while l<=h:
            if h-l<=1: break  ##当m=l的时候，可能永远不会再动了。 停止
            m = (l+h)/2
            if arr[m][-1]==x: return True
            elif arr[m][-1]<x:  l=m     #这里是稍微不一样    #当m=l的时候，可能永远不会再动了。 停止
            else:  h=m
        #然后肯定在h, 或者L
        return x in arr[l] or x in arr[h]      # O( sqrt(N) )  in worst case

