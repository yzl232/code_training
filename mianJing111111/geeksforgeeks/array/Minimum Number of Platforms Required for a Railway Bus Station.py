# encoding=utf-8
'''
Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop

Examples:

Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
        dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)

'''
#就是会议室问题。
class Solution:
    def find(self, arr, dep):
        arr.sort();  dep.sort()
        cnt = 0; n=len(arr); ret=0
        i=j=0
        while i<n and j<n:
            if arr[i]<dep[j]:
                cnt+=1;  i+=1
            else:
                cnt-=1;  j+=1
            ret = max(cnt, ret)
        return ret