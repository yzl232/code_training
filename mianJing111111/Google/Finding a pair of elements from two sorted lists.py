# encoding=utf-8
'''
Finding a pair of elements from two sorted lists(or array) for which the sum of the elements is a certain value. Anyway solution that can do better than O(a.length + b.length)?

我第一直觉是用hashtable
O(m)+O(n)      O(min(m, n))
'''

'''
如果没有排好序，   hash已经是最好的方法了。

但是已经排序了， 更好的方法是没有space.

那就是来自于  Search in a row wise and column wise sorted matrix

如果是完全排序(第一个arr所有值比第二个所有值小)，可以做到log(m+n).

不是完全排序。 只能做到m+n


'''

'''
Given two arrays A and B such that either their length is same or one of them is longer. Let say if A is longer then,
indexA = 0; indexB = B.length -1;
initialize sum = B[indexB] + A[indexA].
while(indexA < A.length && indexB >= 0)
{
if( sum == target )
done
else if( sum > target )
indexB--;
else
indexA++;
}

Time complexity - We can think of above traversal as diagonal traversal that we do in sorted matrix to find a element, which will have complexity O(A.length + B.length ).

We can improvise above logic, by doing binary search on the hypothetical diagonal (0,0) to (A.length, B.length ) and follow the same logic for searching the element in a sorted matrix.
总的来说，hash仍然是最好的，秒杀的，全面的方法

'''

class Solution:
    def searchAB(self, a, b , target):
        i=0; j = len(b)-1
        while i<len(a) and j>=0:
            s = a[i]+b[j]
            if s==target:
                return (i, j)
            elif s>target:    j-=1
            else: i+=1