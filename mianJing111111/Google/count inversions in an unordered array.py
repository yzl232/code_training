# encoding=utf-8
#G家有考.  找逆序对数目
'''

Count Inversions in an array

Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Example:
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
'''

class Solution:
    def merge2(self, part1, part2):#就增加了一行。
        result = []
        i=j=0
        while i<len(part1) and j<len(part2): #就增加了一行。
            if part1[i]<=part2[j]:
                result.append(part1[i])
                i+=1
            else:
                result.append(part2[j])
                self.cnt+=len(part1)-i   #第一个序列右边的都符合。       关键.
                j+=1
        if i<len(part1): result+=part1[i:]      #j=length, 之前都加过了比part2[-1]大的数。
        if j<len(part2):result+=part2[j:]    #i=length  右边的数目为0
        return result
    def mSort(self, arr):
        if len(arr)<2:    return arr
        m = len(arr)/2
        left = self.mSort(arr[:m])
        right = self.mSort(arr[m:])
        return self.merge2(left, right)

    def incnt(self, arr):    #用了一个全局变量
        self.cnt = 0
        self.mSort(arr)
        return self.cnt


#G家考过。
'''
输入一个数组，返回数组元素的surpasser个数的最大值。

数组元素a【i】的surpasser是指元素a[j], j > i， a[j] > a【i】
'''
class Solution6:
    def merge2(self, part1, part2):#就增加了一行。
        result = []
        i=j=0
        while i<len(part1) and j<len(part2): #就增加了一行。
            if part1[i]<part2[j]:
                result.append(part1[i])
                self.cnt+=len(part2)-j   #第2个序列右边的都符合。       关键.
                i+=1
            else:
                result.append(part2[j])
                j+=1
        if i<len(part1): result+=part1[i:]      #j=length, 之前都加过了比part2[-1]大的数。
        if j<len(part2):result+=part2[j:]    #i=length  右边的数目为0
        return result
    def mSort(self, arr):
        if len(arr)<2:    return arr
        m = len(arr)/2
        left = self.mSort(arr[:m])
        right = self.mSort(arr[m:])
        return self.merge2(left, right)

    def incnt(self, arr):    #用了一个全局变量
        self.cnt = 0
        self.mSort(arr)
        return self.cnt

s = Solution()
print s.incnt([2, 4, 1, 9])
s = Solution6()
print s.incnt([2, 4, 1,9])