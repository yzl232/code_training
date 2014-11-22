# encoding=utf-8
'''
Initially there is a number n written on board. Two players start playing a game turn by turn. Each player has to replace the number n written on the board by n-2^k (for some k >= 0 such that 2^k < n)?

Also the number n-2^k has to be as beautiful as n (The beauty of a number depends on the number of one's in its binary representation). The player loses the game when he can't select any such k.
Given the initial number n, determine which player will win the game if both players play optimally. n > 0 and n <= 10^9.



大概看明白了情况。 就是1不断的平移。
1100->1010->1001->0101->0011

1移动一位，就是减去2的k次方。 k取决于在第几位。


当一全部在最右边。 结束了。
解释。

As oldtimer said, the game ends when all ones are on the least significant bits.
So we basically need to count how many swaps we need to make the zeros go to the most significant bits.
For each bit set to 1, the number of swaps needed is equal to the number of 0s in the least significant bits.
If the total number of swaps is odd, player A wins, else B wins.
每一个1. 取决于右边0的数目。

总的step数目， 就是sum of (每一个1. 取决于右边0的数目。)
total为奇数。 player1赢。 else


For the input n, in binary format "100101", the first player, A will lose the game, and the second player B, will win. BC, A can change n to "100011" or "10101", at the first round. For "100011", B can easily win the game. For "10101", B can win the game by change it to "10011".
We can change the model of this problem to the following. Considering there are several buckets, in each of them, there are some balls (means the number of '0'), or, nothing. For instance, "100101" can be represented by 2 buckets, the first bucket has 2 balls and second has 1. Then, for each player, he can pick one bucket and move one ball from the this bucket (ith one) to the (i - 1)th bucket. Of cause, we can only move the ball forward. The guy that moves the last ball win the game.



 解法是O(n)
'''
class Solution:
    def selectWinner(self, n):
        total = 0
        numZeros = 0

        while n!=0:
            if n&1:  #二进制最右边一位是不是1
                total += numZeros
            else:
                numZeros+=1
            n = n>>1  #右移一位。
        return total%2