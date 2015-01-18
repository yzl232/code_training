# encoding=utf-8
'''
 果然是leetcode变体
 因为是纯反向。 改2个符号就可以了
'''
#举出有增加有减少的例子。 238751
##举个例子就容易写。 687432   =》  找到 6， 和7交换。  =》786432=>723468
#  52468  =>   找到5，4 => 42568=> 48652        实际上是逆序的过程。
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, arr):
        n = len(arr)
        for i in range(n-1, 0, -1):
            if arr[i]<arr[i-1]:  #就是大于号变成小于号的过程
                for j in range(n-1, i-1, -1):
                    if arr[j]<arr[i-1]: break
                arr[j], arr[i-1] = arr[i-1], arr[j]
                l = i; r = n-1
                while l<r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l+=1; r-=1
                return arr
        arr.reverse()
        return arr
#是O(n)的
s = Solution()
print s.nextPermutation([2, 1, 5, 6, 7])