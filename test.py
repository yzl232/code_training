#暴力是O(n3).  可以优化求min, max的过程。 到O（n2）
class Solution:
    def dpremoval(self, arr):
        ret = (0, -1);  n = len(arr)
        for start in range(n):
            minN=maxN = arr[start]
            for end in range(start, n):
                minN = min(minN, arr[end])
                maxN = max(maxN, arr[end])
                if 2*minN<=maxN: break
                if end-start>ret[1]-ret[0]: ret = (start, end)
        return arr[ret[0] : ret[1]+1]