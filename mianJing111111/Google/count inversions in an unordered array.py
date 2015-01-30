# encoding=utf-8
#G家有考.  找逆序对数目
'''

Count Inversions in an array

Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Example:
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

#inversion个数从0~ C(n, 2) 都有可能

'''

#因为是排好序的。
# 另外因为调用merge的时候  part1前半。 part2后半。 这是保证的
class Solution:
    def merge2(self, part1, part2):#就增加了一行。
        ret = [];   i=j=0
        while i<len(part1) and j<len(part2): #就增加了一行。
            if part1[i]<=part2[j]:
                ret.append(part1[i]);   i+=1
            else:   #发现逆序！！！
                ret.append(part2[j])
                self.cnt+=len(part1)-i   #第一个序列右边的都符合。       关键.
                j+=1    #j=length, 之前都加过了比part2[-1]大的数。  #i=length  右边的数目为0
        return ret+part1[i:]+part2[j:]

    def mSort(self, arr):
        if len(arr)<2:    return arr
        m = len(arr)/2
        return self.merge2(self.mSort(arr[:m]), self.mSort(arr[m:]))  #先写好( self.msort(),  self.msort()  ) 再填上就好

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
        ret = [];   i=j=0
        while i<len(part1) and j<len(part2): #就增加了一行。
            if part1[i]<part2[j]:
                ret.append(part1[i])
                self.cnt+=len(part2)-j   #第2个序列右边的都符合。       关键.
                i+=1
            else:
                ret.append(part2[j]);   j+=1    #j=length, 之前都加过了比part2[-1]大的数。  #i=length  右边的数目为0
        return ret+part1[i:]+part2[j:]

    def mSort(self, arr):
        if len(arr)<2:    return arr
        m = len(arr)/2
        return self.merge2(self.mSort(arr[:m]), self.mSort(arr[m:]))

    def incnt(self, arr):    #用了一个全局变量
        self.cnt = 0
        self.mSort(arr)
        return self.cnt

s = Solution()
print s.incnt([2, 4, 1, 9])
s = Solution6()
print s.incnt([2, 4, 1,9])