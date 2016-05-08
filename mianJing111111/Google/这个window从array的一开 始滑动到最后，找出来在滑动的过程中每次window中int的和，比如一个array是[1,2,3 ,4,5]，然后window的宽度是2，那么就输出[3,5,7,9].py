# encoding=utf-8
'''
这个window从array的一开
始滑动到最后，找出来在滑动的过程中每次window中int的和，比如一个array是[1,2,3
,4,5]，然后window的宽度是2，那么就输出[3,5,7,9]
'''
class Solution:
    def solve(self, arr, w):
        x = len(arr)-w+1
        assert x>=0
        cur = sum(arr[:w]);  ret=[cur]
        for l in range(1, x):
            r = l+w-1
            cur+=arr[r]-arr[l]
            ret.append(cur)
        return cur
