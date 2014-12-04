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
    def nextPermutation(self, num):
        n = len(num)
        for i in range(n-1, 0, -1):
            if num[i]<num[i-1]:
                for j in range(n-1, i-1, -1):
                    if num[j]<num[i-1]: break
                num[j], num[i-1] = num[i-1], num[j]
                l = i; r = n-1
                while l<r:
                    num[l], num[r] = num[r], num[l]
                    l+=1; r-=1
                return num
        num.reverse()
        return num
#是O(n)的
s = Solution()
print s.nextPermutation([2, 1, 5, 6, 7])