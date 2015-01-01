# encoding=utf-8
'''
Implement below function.
int getRandom(int N, int K[])

Constraints:
->K is sorted and contains elements in range [0,N)
->Output should be a random number between [0,N) excuding elements from K
->probability of generated number should be 1/(N-K.length) and not 1/N
-->int uniform(int N) is given which returns random number [0,N) with 1/N probability for each number.
->No more than O(1) memory
->No more than O(N) time
'''
#背下。不大理解.  出现好多次哦。
import random
class Solution:
    def randK(self, arr, n):
        x = random.randint(0, n-len(arr)-1)
        for jump in range(len(arr)):
            if jump+x<arr[jump]:   return jump+x  #临界是jump+x==arr[jump]
        return len(arr)+x
#极端情况0, 1, 2 ,3
 #   def cntLessOrEqual(self, ):

s = Solution()
for i in range(3):
    print s.randK([1, 2, 4], 6)




'''
import random
class Solution:
    def randK(self, arr, n):
        x = random.randint(0, n-len(arr)-1)
        t = self.bs(x, arr)
        print 'random', x
        if t==-1: return x
        x = x+1+t
        t = self.bs(x, arr[t+1:])
        if t==-1: return x
        return x+1+t

    def bs(self, x, arr, l=0):
        l = 0; h=len(arr)-1
        while l<=h:
            m = (l+h)/2
            if arr[m]==x: return m
            elif arr[m]>x:  h=l-1
            else:  l=m+1
        return h

s = Solution()
for i in range(3):
    print s.randK([1, 2, 4], 6)
'''
import random
class Solution:
    def randK(self, arr, n):
        x = random.randint(0, n-len(arr)-1)
        for jump in range(len(arr)):
            if jump+x<arr[jump]:   return jump+x
        return len(arr)+x
#极端情况0, 1, 2 ,3
 #   def cntLessOrEqual(self, ):

s = Solution()
for i in range(3):
    print s.randK([1, 2, 4], 6)
