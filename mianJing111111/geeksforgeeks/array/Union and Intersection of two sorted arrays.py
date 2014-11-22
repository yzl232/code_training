# encoding=utf-8
'''

Union and Intersection of two sorted arrays


For example, if the input arrays are:
arr1[] = {1, 3, 4, 5, 7}
arr2[] = {2, 3, 5, 6}
Then your program should print Union as {1, 2, 3, 4, 5, 6, 7} and Intersection as {3, 5}.

Algorithm Union(arr1[], arr2[]):
For union of two arrays, follow the following merge procedure.
1) Use two index variables i and j, initial values i = 0, j = 0
2) If arr1[i] is smaller than arr2[j] then print arr1[i] and increment i.
3) If arr1[i] is greater than arr2[j] then print arr2[j] and increment j.
4) If both are same then print any of them and increment both i and j.
5) Print remaining elements of the larger array.

可以都先去重复。 然后做。
另外像这种2 pointer的题目，都可以用hash做。

2sum  leetcode因为没有排序。 用hash是最好的方法了。
如果排序的话， 用2 pointer 可以省下空间。

'''

class Solution:
    def printUnion(self, arr1, arr2):
        result = []
        m = len(arr1);  n = len(arr2)
        i=j=0
        while i<m and j<n:
            if arr1[i] < arr2[j]:
                result.append(arr1[i])  #要去重复的话，每次append之前加一句if i>0 and result[-1]!=arr1[i]:
                i+=1
            elif arr2[j] < arr1[i]:
                result.append(arr2[j])
                j+=1
            else:
                result.append(arr1[i])   #只要i+=1就可以打破平衡了。 够了。
                i+=1
        return result

    def printIntersection(self, arr1, arr2):
        i=j=0; result = []
        m = len(arr1);  n = len(arr2)
        while i<m and j<n:
            if arr1[i] < arr2[j]:  i+=1
            elif arr1[i]> arr2[j]: j+=1
            else:
                result.append([arr1[i]])   #只要i+=1就可以打破平衡了。 够了。
                i+=1