# encoding=utf-8
'''
single number，数组有序，要log(n)

binary search


分析：  奇数，偶数  index

随便找个例子就可以推出来。

01 23 45 6 78 910
11 22 33 4 55 66



'''


class Solution:
    def singleNumber(self,  arr):
        start = 0;  end = len(arr)-1
        while start<=end:
            m = start+(end-start)/2
            if m== start and m==end:   return arr[m] #只有一个元素了。 肯定OK。  而且避免了边界情况
            if m%2==0:
                if arr[m]==arr[m+1]:    start = m+2   #在右边  -- -- -偶数index
                elif arr[m] == arr[m-1]:  end = m-2
                else: return arr[m]
            if m%2==1:
                if arr[m]==arr[m+1]:  end = m-1
                elif arr[m] == arr[m-1]: start=m+1
                else: return arr[m]
s = Solution()
print s.singleNumber([1,1,2,2,3,4,4,9,9])