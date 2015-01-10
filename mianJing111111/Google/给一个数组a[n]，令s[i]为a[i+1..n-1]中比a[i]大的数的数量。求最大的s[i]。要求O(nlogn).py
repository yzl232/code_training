# encoding=utf-8
#给一个数组a[n]，令s[i]为a[i+1..n-1]中比a[i]大的数的数量。求最大的s[i]。要求O(nlogn)

#就是count inversion的变体。




class Solution6:
    def merge2(self, part1, part2):#就增加了一行。
        ret = []
        i=j=0
        while i<len(part1) and j<len(part2): #就增加了一行。
            if part1[i][0]<part2[j][0]:
                ret.append(part1[i])
                self.cnt[part1[i][1]]+=len(part2)-j   #第2个序列右边的都符合。       关键.
                i+=1
            else:
                ret.append(part2[j])
                j+=1
        if i<len(part1): ret+=part1[i:]      #j=length, 之前都加过了比part2[-1]大的数。
        if j<len(part2):ret+=part2[j:]    #i=length  右边的数目为0
        return ret

    def mSort(self, arr):
        if len(arr)<2:    return arr
        m = len(arr)/2
        left = self.mSort(arr[:m])
        right = self.mSort(arr[m:])
        return self.merge2(left, right)

    def incnt(self, arr):    #用了一个全局变量
        self.cnt = [0 for i in range(len(arr))]
        arr = [ (arr[i], i)  for i in range(len(arr)) ]
        self.mSort(arr)
        print self.cnt
        return max(self.cnt)

s = Solution6()
print s.incnt([2, 4, 1, 3, 7, 5, 2])