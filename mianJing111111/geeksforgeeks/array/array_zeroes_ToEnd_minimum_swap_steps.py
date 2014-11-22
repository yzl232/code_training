# encoding=utf-8
'''
http://www.geeksforgeeks.org/move-zeroes-end-array/



Move all zeroes to end of array

Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

There can be many ways to solve this problem. Following is a simple and interesting way to solve this problem.
Traverse the given array ‘arr’ from left to right. While traversing, maintain count of non-zero elements in array. Let the count be ‘count’. For every non-zero element arr[i], put the element at ‘arr[count]‘ and increment ‘count’. After complete traversal, all non-zero elements have already been shifted to front end and ‘count’ is set as index of first 0. Now all we need to do is that run a loop which makes all elements zero from ‘count’ till end of the array.

fast, slow
这里的做法是覆盖法。 用一个指针覆盖。 O(1),  space.  O(n) time
'''

class Solution:
    def pushZeroesToEnd(self, arr):
        slow = 0;  n = len(arr)
        for fast in range(n):
            if arr[fast] !=0:
                arr[slow] = arr[fast]
                slow+=1
        while slow<n:
            arr[slow]=0
            slow+=1
        return arr
s = Solution()
print(s.pushZeroesToEnd([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]))


'''
上面的方法是保证非0数相对顺序。


如果没有这个相对顺序要求，
2个指针swap的方法。 保证了minumum step
'''

class Solution:
    def segregate0and1(self, arr):
        l=0; r = len(arr)-1
        while l<r:
            while arr[l]!=0 and l<r:
                l+=1
            while arr[r]==0 and l<r:
                r-=1
            if l<r:
                arr[l], arr[r] = arr[r], arr[l]  #交换
                l+=1
                r-=1







'''
和segregate  0s  1s 没有区别
'''


class Solutio4n:
    def segregate0and1(self, arr):
        l=0; r = len(arr)-1
        while l<r:
            while arr[l]==0 and l<r:
                l+=1
            while arr[r]==1 and l<r:
                r-=1
            if l<r:
                arr[l], arr[r] = arr[r], arr[l]  #交换
                l+=1
                r-=1


'''
leetcode palindrome
'''
class Solutio2n:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i=0; j = len(s)-1; s = s.lower()
        while i<j:
            while i<j and not ('a'<=s[i]<='z' or '0'<=s[i]<='9'): i+=1
            while i<j and not ('a'<=s[j]<='z' or '0'<=s[j]<='9'): j-=1
            if s[i] != s[j]: return False
            i+=1;   j-=1
        return True
