# encoding=utf-8
'''
session 1一个class {int a,  bool c, int b} 里面每个variable所占的空间都不同
，比如a,b是int 所以分别占4byte. bool的c只占1byte。还有其他变量，可能占8bytes
或者16bytes。都是2的次方就是。
问题是写一个程序让他们可以很好的被放到8byte为单位的block里面去然后空间不会浪
费。
比如如果是 就按照a, c, b的话它一共要占12个byte。因为当把a和c放到一个block的
时候就会浪费一些空间。
所以最好摆成a，b，c这样的话更合理。占9个byte。剩下的空间还可以放一些小的
object。
其实这个就是用排序，然后从大的变量依次放进block。
有个followup的问题就是：因为我不想过多移动这些变量，所以怎么才能设计一个算法
所需要移动的object最少。
比如如果变量的size一次是4, 4, 1, 1, 8, 8, 1, 1最好的排法是4, 4, 8, 8, 1, 1, 1, 1.而不是8 8 4 4 1 1 1 1因为前一种所需要移动的cost最小。这个没想出来了。。
应该用divide and conquer？
'''

#其实这个就是用排序，然后从大的变量依次放进block。
# 贪心的思想

'''
1. 变量的值在{1，4，8，16} 中间，直接group就可，不需排序，找出相同值连续最多
的同一值group,把其他零碎的移过来即可。
'''

#follow up
#首先第一一定要优先满足padding的要求。  如果是8 的倍数， 就跳过，排序后面.   一旦发生不是8的倍数。 没办法了。 只能排序了。 后面统统排序。
#  4, 4, 1, 1, 8, 8, 1, 1最好的排法是4, 4, 8, 8, 1, 1, 1, 1.
# 例子  1  16  4 1 1 1
#   1
# follow up 也就是普通的排序， 稍稍优化。
# 好像不满足follow up 的要求。  比如 4 8  4   16
  #小于8是不可以的。
class Solution:
    def arrange(self, arr):
        s = 0; pre=0
        for i in range(len(arr)): #<=8略去。 一旦大于8且不为16，
            s+=arr[i]
            if s >8 and s%8!=0: break
            elif s%8==0:
                s=0; pre = i+1
        return  arr[:pre]+sorted(arr[pre:], reverse=True)
s = Solution()
print s.arrange([4, 4, 1, 1, 8, 8, 1, 1])
print s.arrange([1, 1, 1, 1,1,1,1,1, 4, 4, 8, 8])