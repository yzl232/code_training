# encoding=utf-8
'''
Question was on Arithmetic progression

Example :
Given the AP :- 1 3 7 9 11 13 find the missing value "which would be 5 here".

Conditions :
Get an user for the length of AP sequence and make sure user provides length is above 3.
Get the input in a single line ex:- "1 3 5 7 9 11"
Provide the solution in O(n) or less if you can.


 O(n)的2种做法：
 we can loop from left to right until we find a difference double any other difference.
如果没找到。 则第一个或者最后一个。

 或者
 S = (N/2)(First Term + Last Term);
 求real  Sum
S- real Sum.   如果为0 。 则第一个或者最后一个。


O(logN)    binary search

'''
# F家
class Solution:
    def missing(self, arr):
        assert len(arr)>=3
        diff = min(arr[2]-arr[1], arr[1]-arr[0])
        l=0; h=len(arr)-1
        while l<h:
            if h-l==1: return (arr[h]+arr[l])/2  #核心在这句。  找到左右边界。 就找到了
            m=(l+h)/2
            leftDiff = arr[m]-arr[l]
            if abs(leftDiff)>abs(diff*(m-l)):  h=m  #左边  不是+1.  比如  1 5 7    边界可能就是m
            else: l=m  #右边
        return -1
s = Solution()
print s.missing([1, 3, 5, 7 ,11, 13])