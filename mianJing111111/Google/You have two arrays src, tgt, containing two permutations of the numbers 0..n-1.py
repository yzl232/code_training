# encoding=utf-8
'''
Rearrange an array using swap with 0.

You have two arrays src, tgt, containing two permutations of the numbers 0..n-1. You would like to rearrange src so that it equals tgt. The only allowed operations is “swap a number with 0”, e.g. {1,0,2,3} -> {1,3,2,0} (“swap 3 with 0”). Write a program that prints to stdout the list of required operations.

Practical application:

Imagine you have a parking place with n slots and n-1 cars numbered from 1..n-1. The free slot is represented by 0 in the problem. If you want to rearrange the cars, you can only move one car at a time into the empty slot, which is equivalent to “swap a number with 0”.

Example:
src={1,0,2,3}; tgt={0,2,3,1};
'''

'''
The special case for this is when you swap ZERO into its correct position. In this case, you can't swap the correct number in, because it is already there -- it just happens to be ZERO. Instead, you can swap some other incorrect number into ZERO's position. (just move misplaced number into a different misplaced position -- ZERO's position) In the next iteration after doing this fix, it is guaranteed that you will swap some number into its correct place. So even when this special case occurs, it will still only take 2 swaps to move 1 misplaced number.
'''

#见过。
'''
shuffle. 输入是[0,2,_,3] 输出是[0,_,2,3].  就是一个乱序数组, 其中缺少了一个值, 然后输出, 每个数值都在自己对应的index上面. 但是移动的时候, 只能把数字放在空缺的位置上, 要求移动的次数最少. (这个我也不知道OPTimal的方法是什么)
'''


def rearrage_swap0(src, tgt):
    tgt_0 =tgt.index(0)    #基本上就是0所在的位置。  每次都修正这个位置的value.   直到0也归位。
    print src
    i = src.index(0)
    if tgt_0 == i:  #0已经在正确位置上了。。随便找一个不match的位置。 交换
        for j in range(len(src)):
            if src[j]!=tgt[j]: break
        src[i], src[j] = src[j], src[i]
        print src[i], '<->', src[j], src
        i = j

    while i != tgt_0:
        j = src.index(tgt[i])
        src[j], src[i] = src[i], src[j]
        print src[i], '<->', src[j], src
        i = j

rearrage_swap0([1, 0, 2, 3], [0, 2, 3, 1])
print '========'
rearrage_swap0([1, 0, 2, 3], [2, 0, 3, 1])
print '========'
rearrage_swap0([1, 2, 3, 0], [1, 3, 2, 0])
