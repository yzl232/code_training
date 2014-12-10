# encoding=utf-8
'''
Given a array
{{ 4,7,3,6,7}}

construct a triangle like
{{81}}
{{40,41}}
{{21,19,22}}
{{11,10,9,13}}
{{ 4,7,3,6,7}}
倒三角形

'''
class Solution:
    def construct(self, arr):
        ret =[]
        while arr:
            ret = [arr]+ret
            arr = [arr[i]+ arr[i+1] for i in range(len(arr)-1)]
        return ret
s = Solution()
a =  s.construct([1, 2, 3, 4])
for  i in a:
    print i