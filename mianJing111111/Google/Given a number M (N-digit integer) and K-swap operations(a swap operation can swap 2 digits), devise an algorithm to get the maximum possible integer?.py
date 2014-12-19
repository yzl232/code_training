# encoding=utf-8
'''
Given a number M (N-digit integer) and K-swap operations(a swap
operation can swap 2 digits), devise an algorithm to get the maximum possible integer?
Examples:
M = 132 K = 1 output = 312
M = 132 K = 2 output = 321
M = 7899 k = 2 output = 9987
M = 8799 and K = 2 output = 9987
'''
#太难了。 搞不定。 不搞了。


#非常难的题目。 第一个  排序。  第二步骤： 和原来的arr比较不同的数字。视为to swap。 注意不可以超过k次

#暴力法： DFS。 swap k 次。 求最大。

'''
#O(nlogn + kn)
class Solution:
    def swapK(self, arr, k):
        arrSorted = [arr[i] for i in range(len(arr))]
        arrSorted.sort(reverse=True)  #取值逆序， index顺序
        toSwap = [(arr[i], i, arrSorted[i]) for i in range(len(arrSorted)) if arrSorted[i]!=arr[i]]
        if k>=len(toSwap): return arrSorted
        toSwap = toSwap[:min(2* k, len(toSwap))]  #最好情况。 每次swap搞定2个数字
         #三元组。.  目的同样是替换为8.  较大的数尽量与靠左边的8交换   第一个是原来数组的值， 第二个是index， 第三个是新的值
        toSwap.sort(reverse=True)  #同样是替换为8.  较小的数要替换到更加右边的数。
        while toSwap:
            oldV, i, newV = toSwap.pop()  #同样是替换为8.  较小的数要替换到更加右边的数。
            for j in range(len(arr)-1, -1, -1):
                if arr[j]==newV:    arr[j], arr[i] = arr[i], arr[j]
        return arr

s = Solution()
print s.swapK([8, 7, 9, 9], 1)
print s.swapK([9, 8, 6, 5, 9, 9, 9], 1)
print s.swapK([7, 9, 8, 6, 5, 9, 9, 9], 3)
print s.swapK([4, 9, 8, 6, 5, 8, 7, 9], 2)
print s.swapK([4, 9, 3, 6, 5, 8, 7, 8], 3)
print s.swapK([9, 9, 3, 6, 5, 8, 7, 8], 2)
print s.swapK([9, 9,  6,3, 5, 8, 7, 8], 2)
print s.swapK([3, 1, 2], 2)
print s.swapK([3, 4, 1, 2], 2)
print s.swapK([3, 2, 1, 4], 2)

'''

'''
class Solution:
    def swapK(self, arr, k):
        arr1 = sorted(arr)[::-1]
        start = 0
        cur = arr1[start]
        while k>0 and start<len(arr):
            for i in range(len(arr)-1, start, -1):
                if arr[i]==cur and i!=start:
                    arr[i], arr[start] = arr[start], arr[i]
                    start+=1; k-=1
                    break
            else:
                start+=1
        return arr

s = Solution()
print s.swapK([8, 7, 9, 9], 1)
print s.swapK([7, 9, 8, 6, 5, 9, 9, 9], 1)
print s.swapK([7, 9, 8, 6, 5, 9, 9, 9], 3)
print s.swapK([4, 9, 8, 6, 5, 8, 7, 9], 2)
print s.swapK([4, 9, 3, 6, 5, 8, 7, 8], 3)
print s.swapK([9, 9, 3, 6, 5, 8, 7, 8], 2)
'''


'''
Algorithm:
a. We start at the leftmost digit (current-position=0).
b. We start with the highest digit value (current-digit-value=9).
c. We scan the number and note all the positions of the digits of the current digit value. Example: N=8799 , positions=[2, 3] (the digit 9 is in positions 2 and 3).
d. We put the K digits starting at the current position in a list (if some of these digits are equal or higher then the current digit value, then we skip them). Example: K=2 digits={8, 7} (the 2 digits starting from the current position).
e. Now we swap the rightmost digit from the "positions" list in step c, with the lowest value digit from "digits" list from step d. We repeat this with the next digit in each list, until either list is exhausted. Example: first swap right-most 9 with 7 (lowest value): N=8997, then swap second 9 from right with next leowest digit 8: N=9987.
f. Decrement K by the number of swaps made. Exit if K is zero. Example: K=0
g. Increment current-position similarly. Exit if we reached the end.
h. Decrement current-digit-value (current-digit-value=8). Exit if we reached zero.
i. Repeat steps c,d,e,f,g,h,i

Complexity: O(N)+O(k log k) if implementing the list in step d as a heap.



import heapq


# Complextiy: time O(N)+O(k log k), space O(N)

class Solution:
    def kswaps_int(self, digit, start, k):
        arr = self.arr
        l = [i for i in range(start, len(arr)) if arr[i] == digit]  #找到digit的位置
        c = 0;  t=min(len(l), k)
        h = []
        while c <t and i < len(arr):
            if arr[i] < digit:    heapq.heappush(h, (arr[i], i))  #从前往后找到比 digit小的
            c += 1;   i += 1  #用greedy的思想。 start肯定是前面4个都是9， start第五个
        start = start+len(l)
        print h, 'start', start
        while h and k>0:
            vDigit, vPos = heapq.heappop(h)
            cur = l[-1]   #从后往前     #同样是变成9， 值小的放在后面
            if cur > vPos:    #
                arr[cur], arr[vPos] = arr[vPos], arr[cur]
                l.pop()
                k -= 1
        print self.arr, 'k' ,k,  'start', start
        return (start, k)

    def kswaps(self, arr, k):
        self.arr = arr
        start = 0
        digit = 9    #digit从9到1开始找。 找k个
        while k > 0 and digit >= 0:
            start, k = self.kswaps_int(digit, start, k)
            digit -= 1

s = Solution()
def main():
    m=[7, 9, 8, 6, 5, 9, 9, 9]
    k = 1
    print m, k
    s.kswaps(m, k)
    print m
    print

    m=[4, 9, 8, 6, 5, 8, 7, 9]
    k = 3
    print m, k
    s.kswaps(m, k)
    print m
    print

    m=[4, 9, 3, 6, 5, 8, 7, 8]
    k = 3
    print m, k
    s.kswaps(m, k)
    print m
    print

    m=[9, 9, 3, 6, 5, 8, 7, 8]
    k = 1
    print m, k
    s.kswaps(m, k)
    print m
    print

if __name__ == '__main__':   main()
'''

#思想：  从9到1.  看9的个数，  取t= min(k, cnt(9)).  找出t个数，存入heap。 9从右边往左边交换


