# encoding=utf-8
'''
Majority Element: A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).

Write a function which takes an array and emits the majority element (if it exists), otherwise prints NONE as follows:



'''

#G家考过   O(1) space, O(n)
# sort 后，  arr[n/2]就是。。 O（nlogn）
# hash则要O(n)

'''
算法的基本思想非常简洁: 每次都找出一对不同的元素，从数组中删掉，直到数组为空或只有一种元素。 不难证明，如果存在元素e出现频率超过半数，那么数组中最后剩下的就只有e。当然，最后剩下的元素也可能并没有出现半数以上。比如说数组是[1, 2, 3]，最后剩下的3显然只出现了1次，并不到半数。排除这种false positive情况的方法也很简单，只要保存下原始数组，最后扫描一遍验证一下就可以了。
'''


'''
 现在来分析一下复杂度。删除元素可以在常数时间内完成，但找不同元素似乎有点麻烦。实际上，我们可以换个角度来想，用一个小trick来重新实现下该算法。

在算法执行过程中，我们使用常量空间实时记录一个候选元素c以及其出现次数f(c)，c即为当前阶段出现次数超过半数的元素。在遍历开始之前，该元素c为空，f(c)=0。然后在遍历数组A时，

    如果f(c)为0，表示当前并没有候选元素，也就是说之前的遍历过程中并没有找到超过半数的元素。那么，如果超过半数的元素c存在，那么c在剩下的子数组中，出现次数也一定超过半数。因此我们可以将原始问题转化为它的子问题。此时c赋值为当前元素, 同时f(c)=1。
    如果当前元素A[i] == c, 那么f(c) += 1。(没有找到不同元素，只需要把相同元素累计起来)
    如果当前元素A[i] != c，那么f(c) -= 1 (相当于删除1个c)，不对A[i]做任何处理(相当于删除A[i])

如果遍历结束之后，f(c)不为0，那么再次遍历一遍数组，记录c真正出现的频率，从而验证c是否真的出现了超过半数。上述算法的时间复杂度为O(n)，而由于并不需要真的删除数组元素，我们也并不需要额外的空间来保存原始数组，空间复杂度为O(1)。实际上，在Moore大牛的主页上有针对这个算法的一个演示，感兴趣的同学可以直接移步观看。
'''
#hash是O(n), O(n)



#其他元素看做-1，  这个元素看做1？？。。
class Solution:
    def findMajority(self, arr):
        maj = self.findCandidate(arr)
        if arr.count(maj)<=len(arr)/2: raise ValueError  ## verify  arr[x] really appears more than half  .  O(n)
        return maj    

    def findCandidate(self, arr):
        x =0; cnt=1
        for i in range(1, len(arr)):
            if arr[i]==arr[x]: cnt+=1
            else: cnt-=1
            if cnt==0:  #之前部分没有出现超过半数的元素。 继续到剩下的部分找。
                x=i
                cnt=1
        return arr[x]


'''
一个不错的方法。 O(32 N )

Runtime: O(n) — Moore voting algorithm: We maintain a current candidate and a counter initialized to 0. As we iterate the array, we look at the current element x:
If the counter is 0, we set the current candidate to x and the counter to 1.
If the counter is not 0, we increment or decrement the counter based on whether x is the current candidate.
After one pass, the current candidate is the majority element. Runtime complexity = O(n).
Runtime: O(n) — Bit manipulation: We would need 32 iterations, each calculating the number of 1's for the ith bit of all n numbers. Since a majority must exist, therefore, either count of 1's > count of 0's or vice versa (but can never be equal). The majority number’s ith bit must be the one bit that has the greater count.
Update (2014/12/24): Improve algorithm on the O(n log n) sorting solution: We do not need to 'Find the longest contiguous identical element' after sorting, the n/2th element is always the majority.

public int majorityElement(int[] num) {

    int ret = 0;

    for (int i = 0; i < 32; i++) {

        int ones = 0, zeros = 0;

        for (int j = 0; j < num.length; j++) {
            if ((num[j] & (1L << i)) != 0) {
                ++ones;
            }
            else
                ++zeros;
        }

        if (ones > zeros)
            ret |= (1L << i);
    }

    return ret;
}

'''