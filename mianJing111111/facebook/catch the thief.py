# encoding=utf-8
'''




思路：博弈。最迷惑的地方就是警察每天向一个方向，比如由起点向右边查找房子的时候，小偷有可能来个时间差移动到了警察的左边。

这个问题其实用博弈就可以解决：先假设小偷在编号为偶数的房子内，这从起点向右搜的时候，小偷就不可能移动到警察左边了 (0, 2, 4)。

最坏情况下，从左搜到右都找不到小偷，证明假设不成立 ()

所以可以确定小偷起始必定在编号为奇数的房子内，这种情况下再来一个从左到右搜就必定能找到小偷了。这时候的结果会是2*n，但是还不是最优的，每次判断小偷不在偶数(或奇数)房间的时候，其实可以按一个方向搜1~n-2的房间就可以了，这个证明就略了。

举例子  1， 2， 3， 4
其实可以按一个方向搜1~n-2的房间就可以了
 1，2，3，4，5

 1， 2（n-2） 相差奇数。 一定变化了。


n the Qingshui Village, there's a clever thief and a cleverer police.

There are N houses in Qingshui Village which are located in a straight line. And the N houses are numbered from 1 to N according to the direction of the line. Two houses are consided to be neighbor of each other if and only if there is no other house between them.

The thief hides in one of N houses now, and the police tries to find him out. Every day the police will choose a house to check and he will catch the thief if he hides in that house. If the thief survive the arrest of the police, in the night he will move to a neighboring house to pass through the next day.

What is the number of days the police needs to catch the thief in the worst case?
Remember that the police is a clever man.


 n 个房间，小偷每天偷一间，偷的规律简单说就是随机行走，如果今天偷了第 i 间屋子，明天有一 半的几率偷 i-1，一半的几率偷 i+1，注意如果刚好偷到了边界上，那么第二天只有唯一的选择。如果你 是警察，你只能每天选择一个房间蹲守，并且贼的手段相当高明，偷了一个房间后，没有任何人能发觉该 房间是否曾经被偷过。



 一上来直接code，找小偷问题，有n个房间，其中一个房间有小偷。早上我们可以打开一个房间的门看小偷在不在里面，晚
 上小偷会向左边或者右边的房间走。现在给你一个开门的sequence，你输出这个sequence能不能保证找到小偷。



 比如：如果只有三个房间(0, 1, 2  ) 那么如果打开房间的sequence是{1，1}那么一定会找到小偷。因为如果小偷在中间那么第一天就会被找到，
 如果小偷在两边那么第二天一定回来到中间也会被找到。房间数为n，sequence长度为k.


 跟着我开始brute force假设小偷在某个房间然后dfs所有路径，大概是O（n*n^k）。
  考官说好，如果考虑cut branch呢？
  跟着我就说可以 拿一个n*k的matrix跟着根据sequence来cut branch，reduce到O（n*n*k）。他说有没有可能同时从所有房间开始呢？我说可以跟着直接
 在那个n*kmatrix上做一个类似dp的东西。跟着reduce 到 O（n*k）。他说有没有可能把space reduce呢？我说可以我只要O（n）的space
 跟着他就让我再写一个叫nextRow的function来实现O（n）space。 我觉得这题我基本是答得非常漂亮的而且思路很清晰，考官也很开心。


  题意：在一条直线上，按顺序排着n座房子(编号0~n-1)。现在有一个警察，知道有一个小偷就在这些房子的其中一间内。每一天早上警察都可以查找任意一间房，如果小偷在这间房子内就会被逮捕，如果小偷不在这间房子内，警察就只好等明天早上继续查找另一间房。但是每天警察搜查离开后，晚上小偷又会移动到旁边的房子去躲一天。问最坏清苦下，警察要花几天才能捉到小偷。

'''
class Solution:
    def catchThief(self, n):
        if n==1: return 1
        if n==2: return 2
        return 2*n-4
'''
对的。 逼到死角以后。 不用过去。 在原地停留一天就好


1，n-1 从左往右， 再从右往左 。一定可以。注意 在n-1停留一下

1   假设小偷在偶数位置。  0，2  我们从左往右扫肯定能扫到。
2   假设小偷在奇数位置。 从右往左扫，肯定扫到。


举例子  1， 2， 3， 4
'''