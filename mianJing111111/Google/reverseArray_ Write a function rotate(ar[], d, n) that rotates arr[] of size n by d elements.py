 # encoding=utf-8
'''
比我上次写的代码好看多了。


 array rotation

 Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

 用了临时arr:     return arr[d:] + arr[:d]

假如要O(n),  O(1)


Algorithm:

rotate(arr[], d, n)
  reverse(arr[], 1, d) ;
  reverse(arr[], d + 1, n);
  reverse(arr[], l, n);

Let AB are the two parts of the input array where A = arr[0..d-1] and B = arr[d..n-1]. The idea of the algorithm is:
Reverse A to get ArB. /* Ar is reverse of A */
Reverse B to get ArBr. /* Br is reverse of B */
Reverse all to get (ArBr) r = BA.

For arr[] = [1, 2, 3, 4, 5, 6, 7], d =2 and n = 7
A = [1, 2] and B = [3, 4, 5, 6, 7]
Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]
'''
#G家考过

class Solution2:
    def reverse(self, start, end, arr):
        while start<end:  #都是这种限定start, end的reverse
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1
    def rotate(self, d, arr):
        self.reverse(0, d-1, arr)       #先reverse 2小片
        self.reverse(d, len(arr)-1, arr)
        self.reverse(0, len(arr)-1, arr)
        return arr#再全部reverse
#和leetcode Reverse Words in a String II  比较像

s = Solution2()
print  s.rotate(2, [1,2,3,4,5,6, 7])
