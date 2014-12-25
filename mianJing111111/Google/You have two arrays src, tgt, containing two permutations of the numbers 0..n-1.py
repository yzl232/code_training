# encoding=utf-8
'''
Rearrange an array using swap with 0.

You have two arrays src, tgt, containing two permutations of the numbers 0..n-1. You would like to rearrange src so that it equals tgt. The only allowed operations is “swap a number with 0”, e.g. {1,0,2,3} -> {1,3,2,0} (“swap 3 with 0”). Write a program that prints to stdout the list of required operations.

Practical application:

Imagine you have a parking place with n slots and n-1 cars numbered from 1..n-1. The free slot is represented by 0 in the problem. If you want to rearrange the cars, you can only move one car at a time into the empty slot, which is equivalent to “swap a number with 0”.

Example:
src={1,0,2,3}; tgt={0,2,3,1};
'''
def rearrage_swap0(src, tgt):
    tgt_0 =tgt.index(0)    #基本上就是0所在的位置。  每次都修正这个位置的value.   直到0也归位。
    print src
    i = src.index(0)
    if tgt_0 == i:  #0已经在正确位置上了。。
        j = (i+1)%len(src)
        src[i], src[j] = src[j], src[i]
        print i, '<->', j, src
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
rearrage_swap0([1, 2, 3, 0], [2, 3, 1, 0])
