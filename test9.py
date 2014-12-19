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

import heapq


# Complextiy: time O(N)+O(k log k), space O(N)

class Solution:
    def kswaps_int(self, digit, start, k):
        arr = self.arr
        l = [i for i in range(start, len(arr)) if arr[i] == digit]  #找到digit的位置
        c = len(l)
        h = []
        while c > 0 and start < len(arr):
            if arr[start] < digit:    heapq.heappush(h, (arr[start], start))  #从前往后找到比 digit小的
            c -= 1;   start += 1
        print h
        while h:
            (vDigit, vPos) = heapq.heappop(h)
            cur = l[-1]   #从后往前
            if cur > vPos:   #同样是变成9， 值小的放在后面
                arr[cur], arr[vPos] = arr[vPos], arr[cur]
                l.pop()
                k -= 1
            else:    start -= 1
        print self.arr, k
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
    k = 3
    print m, k
    s.kswaps(m, k)
    print m

    m=[4, 9, 8, 6, 5, 8, 7, 9]
    k = 3
    print m, k
    s.kswaps(m, k)
    print m


if __name__ == '__main__':   main()