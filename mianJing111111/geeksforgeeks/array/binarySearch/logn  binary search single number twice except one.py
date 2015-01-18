# encoding=utf-8
'''
single number，数组有序，要log(n)

binary search


分析：  奇数，偶数  index

随便找个例子就可以推出来。

01 23 45 6 78 910
11 22 33 4 55 66



'''
# F家


#虽然长了一点。 但是逻辑清楚。比较好写
class Solution:
    def singleNumber(self,  arr):
        l = 0;  h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if l==h:   return arr[m]    #只有一个元素了。 肯定OK。  而且避免了边界情况
            if m%2==0:
                if  arr[m]==arr[m+1]:    l = m+2   #在右边  -- -- -偶数index
                elif  arr[m] == arr[m-1]:  h = m-2
                else: return arr[m]
            elif m%2==1:
                if arr[m]==arr[m+1]:  h = m-1
                elif arr[m] == arr[m-1]: l=m+1
                else: return arr[m]
s = Solution()
print s.singleNumber([1,1,2,2,3,4,4,9,9])
print s.singleNumber([1,2, 2])
print s.singleNumber([2,2,4,4,9])