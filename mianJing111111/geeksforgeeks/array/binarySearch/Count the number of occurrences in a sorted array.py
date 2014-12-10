# encoding=utf-8
'''
Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(Logn)

Examples:

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
  Output: 4 // x (or 2) occurs 4 times in arr[]

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
  Output: 1

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 1
  Output: 2

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 4
  Output: -1 // 4 doesn't occur in arr[]
'''


'''
1) Use Binary search to get index of the first occurrence of x in arr[]. Let the index of the first occurrence be i.
2) Use Binary search to get index of the last occurrence of x in arr[]. Let the index of the last occurrence be j.
3) Return (j – i + 1);
'''





class Solution:  #那个majority也有用到。
    def leftS(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==0 or arr[m-1]!=x) and arr[m]==x: return m
            elif arr[m]<x: l = m+1
            else:  h=m-1    #其他时候，相等的时候，也是在左边
        return -1

    def rightS(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==len(arr)-1 or arr[m+1]!=x) and arr[m]==x: return m
            elif arr[m]>x:  h=m-1
            else:   l=m+1
        return -1  #其他时候，相等的时候，也是在右边

    def findCnt(self, arr, x):
        i = self.leftS(arr, x)
        if i==-1: return 0
        j = self.rightS(arr, x)
        return j-i+1

s = Solution()
print s.findCnt([1,2,3, 4, 4, 4, 5], 4)


'''

class Solution:  #那个majority也有用到。
    def leftS(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==0 or arr[m-1]<x) and arr[m]==x: return m
            elif arr[m]<x: l = m+1
            else:  h=m-1    #其他时候，相等的时候，也是在左边
        return -1

    def rightS(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==len(arr)-1 or arr[m+1]>x) and arr[m]==x: return m
            elif arr[m]<=x: l = m+1   #其他时候，相等的时候，也是在右边
            else:  h=m-1
        return -1

    def findCnt(self, arr, x):
        i = self.leftS(arr, x)
        if i==-1: return 0
        j = self.rightS(arr, x)
        return j-i+1

s = Solution()
print s.findCnt([1,2,3, 4, 4, 4, 5], 4)
'''