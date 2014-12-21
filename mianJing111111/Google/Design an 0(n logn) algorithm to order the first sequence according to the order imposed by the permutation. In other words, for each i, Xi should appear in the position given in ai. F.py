# encoding=utf-8
'''
The input is a sequence x1,x2,...,xn of integers in an arbitrary order, and another sequence
a1,a2,..,an of distinct integers from 1 to n (namely a1,a2,...,an is a permutation of
1, 2,..., n). Both sequences are given as arrays. Design an 0(n logn) algorithm to order
the first sequence according to the order imposed by the permutation. In other words, for
each i, Xi should appear in the position given in ai. For example, if x = 17, 5, 1,9, and a =
3, 2, 0, 1, then the outcome should be x = 9, 1, 17, 5. The algorithm should be in-place, so
you cannot use an additional array.
'''

#很巧妙。 可以背下
class Solution:
    def sortArr(self, arr, iarr):
        for i in range(len(arr)-1):     #最后一下不用交换了。 因为只和>=i的index交换
            x = iarr[i]
            while x<i: x=iarr[x]  #就是防止已经搬运过的情况。  也就是swap的判定是order的。 只swap一次
            arr[i], arr[x] = arr[x], arr[i]   #正确的index是3， 把arr[3]搬过来
            print arr, arr[i], arr[x]
        return arr
s = Solution()
print s.sortArr([17, 5, 1, 9], [3, 2, 0, 1])
print s.sortArr([17, 5, 1, 9], [1, 3, 2, 0])

'''
it works because you're first checking where 1 goes in the permutation. then you check where 2 goes. but you only go to an new index farther or equal to the current index. this makes sure you don't double swap. the reason why the while loop always ends is because the iteration a = As[a] will always and come back to i again (in n or less iterations). you're basically iterating through the different cycles in the cycle decomposition of the permutation
'''