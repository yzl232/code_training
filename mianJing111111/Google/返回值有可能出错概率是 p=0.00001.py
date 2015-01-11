# encoding=utf-8
'''
有一个函数
long compute(int i) {
 return …;
}
返回值有可能出错概率是 p=1/10000。

还有一个函数
long total(int n) {
 long s = 0;
 for (int i =0; i < n; i++) {
   s += compute(i);
 }
 return s;
}
这样出错概率就是 np;

问： 如何改第二个函数，让他的出错概率小于p?
我的思路是，for 循环里,再加个循环，写了代码。 最后老印说work, 大多人都这么做
，好像他不满意。这个题怎么做？
'''

'''
第二题，如果compute(i)是p，那么连续两次都出错的概率就是p^2 （连续调用直到连
续两次得到的结果相同），根据n的大小，连续调用compute(i)多次，使得最终的概率
小于p
'''