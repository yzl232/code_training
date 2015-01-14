# encoding=utf-8
'''
We can write a 3 level for loop body directly as follows:
    for (int i  = 0;  i < 56; ++i){
                do_something(i);
                for(int j = 0; j < 151; ++j){
                        do_something(j);
                        for(int k = 0; k < 151; ++k){
                                do_something(k);
                        }
                }
    }
    However, when the levels are very deep (such as 50 levels), we cannot manually write the for loop body directly just like above codes.

    Given an array arr, where arr[i] represents the loop count at level i, write an iterative algorithm to implement the multi-level loop.
'''



#怎么记忆代码？  就是模拟dfs的过程。

#有点像数的相加。 每次本层满了。  上一层+1。 比较像plus one
#也比较像DFS。 combination。 到了底层， 回到上一层。 模拟dfs


class Solution:
    def solve(self, arr, n):
        if n==0: return
        i=0
        cnt = [0]*(n)
        while i>=0:
            if i==n or cnt[i] == arr[i]:   #本层满了。开始上一层。
                i-=1
                if i>=0:  cnt[i]+=1
            else:
                self.doSomething(i)
                i+=1
                if i<n: cnt[i]=0
            #print cnt, i

    def doSomething(self, x):
        print x

'''
    for(int i = 0; i < levelCountArr[0]; ++i) {
    do_operation(i);
    for(int j = 0; j < levelCountArr[1]; ++j) {
    do_operation(j);
    for(int k = 0; k < levelCountArr[2]; ++k) {
    do_operation(k);
    for(int l = 0; l < levelCountArr[3]; ++l)
    do_operation(l);
    }
'''

#http://www.tutorialspoint.com/compile_cpp_online.php
# 开始看的很糊涂。 原来这22行是第四层12+第三层6+第2层2+第一层2。。 共22行。
s= Solution()
print s.solve([2, 1, 3, 2], 4)