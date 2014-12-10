# encoding=utf-8
'''
Merge k sorted arrays | Set 1

Given k sorted arrays of size n each, merge them and print the sorted output.

Example:

Input:
k = 3, n =  4
arr[][] = { {1, 3, 5, 7},
            {2, 4, 6, 8},
            {0, 9, 10, 11}} ;

Output: 0 1 2 3 4 5 6 7 8 9 10 11

A simple solution is to create an output array of size n*k and one by one copy all arrays to it. Finally, sort the output array using any O(nLogn) sorting algorithm. This approach takes O(nkLognk) time.


类似leetcode那道题。 用merge sort.      nklog(k).


Recursive Algo:
void mergeK(int a[][MAX],int low,int high,int n){
1: if(low>=high)
return;
2 : int mid=(low+high)/2;
3: mergeK(a,low,mid,n);
4 : mergeK(a,mid+1,high,n);
// now merge two sorted array a[low][n] to a[high][n]
5 : merge(arr, low*n, (mid+1)*n ,(mid+1)*n, (high+1)*n);
}





变体是这个n=k的情况。 类似的。


Print all elements in sorted order from row and column wise sorted matrix

Given an n x n matrix, where every row and column is sorted in non-decreasing order. Print all elements of matrix in sorted order.

Example:

Input: mat[][]  =  { {10, 20, 30, 40},
                     {15, 25, 35, 45},
                     {27, 29, 37, 48},
                     {32, 33, 39, 50},
                   };

Output:
Elements of matrix in sorted order
10 15 20 25 27 29 30 32 33 35 37 39 40 45 48 50



'''

import heapq

#heap和merge 复杂度一样。 但是heap代码只有8行。 merge代码要三倍


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, arrs):
        h =[(arrs[i][0], i, 0) for i in range(len(arrs)) if arrs[i]]
        heapq.heapify(h);  ret = []
        while h:
            pop = heapq.heappop(h)
            val, i, j = pop[0], pop[1], pop[2]
            ret.append(val)
            if j+1<len(arrs[i]):  heapq.heappush(h, (arrs[i][j+1], i, j+1))
        return ret   #复杂度 O(nkLogk) 是最优解




#和heap和merge sort复杂度一样
'''
class Solution:
    def mergeK(self, matrix):
        if len(matrix)<=1: return matrix
        while len(matrix)>1:
            newLists = []
            for i in range(0, len(matrix)-1, 2):
                newLists.append(self.merge2(matrix[i], matrix[i+1]))
            if len(matrix)%2==1: newLists.append(matrix[-1])
            matrix = newLists
        return matrix[0]


    def merge2(self, part1, part2):
        result = []
        i=j=0
        while i<len(part1) and j<len(part2):
            if part1[i]<part2[j]:
                result.append(part1[i])
                i+=1
            else:
                result.append(part2[j])
                j+=1
        if i<len(part1): result+=part1[i:]
        if j<len(part2):result+=part2[j:]
        return result
s = Solution()
print s.mergeK([[1, 3, 5], [2, 4, 9], [3, 4, 5]])
'''
s = Solution()
print s.mergeKLists([[1, 3, 5], [2, 4, 9], [3, 4, 5]])