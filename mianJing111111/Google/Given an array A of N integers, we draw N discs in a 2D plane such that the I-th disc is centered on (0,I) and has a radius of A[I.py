# encoding=utf-8
'''
Given an array A of N integers, we draw N discs in a 2D plane such that the I-th disc is centered on (0,I) and has a radius of A[I]. We say that the J-th disc and K-th disc intersect if J ≠ K and J-th and K-th discs have at least one common point.
Write a function:
int number_of_disc_intersections(int A[], int N);
that, given an array A describing N discs as explained above, returns the number of pairs of intersecting discs. For example, given N=6 and:
A[0] = 1 A[1] = 5 A[2] = 2
A[3] = 1 A[4] = 4 A[5] = 0
intersecting discs appear in eleven pairs of elements:
0 and 1,
0 and 2,
0 and 4,
1 and 2,
1 and 3,
1 and 4,
1 and 5,
2 and 3,
2 and 4,
3 and 4,
4 and 5.
so the function should return 11.
The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
Assume that:
N is an integer within the range [0..10,000,000];
each element of array A is an integer within the range [0..2147483647].
Complexity:
expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
'''

'''
rearrange them in the format of interval: [-1,1] [-4,6] ...
then the problem becomes checking overlapping intervals.
just sort them on the base of starting point and binary search each end point in the sorted list
'''
class Solution:
    def cnt(self, arr):
        affairs = [];   ret = 0; d={}
        for i in range(len(arr)):
            affairs.append((i-arr[i], 0, i))
            affairs.append((i+arr[i], 1, i))
            d[i] = 0
        affairs.sort()
        sCnt = 0;     eCnt=0
        for x in affairs:
            if x[1]==0:
                sCnt+=1
                d[x[-1]]=-eCnt
            elif x[1]==1:
                eCnt+=1
                d[x[-1]]+=sCnt-1
        return sum(d.values())/2        #end


'''
    def bsearch(self, start, x, arr):  #start的数目就是i了。 end的数目就是binary search了。
        l =start; h=len(arr)-1
        while h>l:  #float型的binary search。 可以把accuracy提前到前面。 少了一行
            if h-l==1: break
            m =(l+h)/2
            if arr[m]>x:  h = m
            else: l=m
        return int(l-start)
'''
s = Solution()
print s.cnt([1, 5, 2 ,1 ,4 ,0])