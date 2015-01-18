# encoding=utf-8
'''
给一个unsigned int数组，size为n，数组的sum = a，计算一个k的值，将数组中
所有大于k的数改为k之后，数组的sum变为b。Ex,  [1,2,5,7,7,8] = a = 30, b = 26,
                         那么k = 6，因为[1,2,5,6,6,6] = 26。


for example:
[4,6,87,93,46,8] = 244
50 = k
target [4,6,50,50,46,8] = 164

after sort [4,6,8,46,87,93]

4 * 6 = 24
[2,4,42,83,89]
2 * 5 = 10 + 24 = 34
[2,40,81,87]
2 * 4 = 8 + 34 = 42
[38,79,85]
38 * 3 = 114 + 42 = 156
[41, 47]
we don't keep going because 156 + 41 > 164
there are 2 numbers left in the array.
so, 164 - 156 = 8
46 + 8/2 = 50, this is the k we want

'''



class Solution:
    def findK(self, arr, target):
        if not arr: raise ValueError()    #空得话，一般raise  valueError。  其他的assert就好
        n = len(arr); cur = 0
        arr.sort()  #先排序。 然后找那个值。
        for i in range(n):
            if arr[i]*(n-i) + cur>target:  break
            cur+=arr[i]   #curSum + 找到了这个值！！！
        return (target-cur)/(n-i)     #上面这行反过来而已。
s = Solution()
print s.findK([4,6,87,93,46,8], 164)
print s.findK( [1,2,5,7,7,8], 26)
print s.findK([1,2,5,7,7,8],   29)
print s.findK([4, 4, 4, 4, 3],  15)
print s.findK([50, 50, 2],   10)