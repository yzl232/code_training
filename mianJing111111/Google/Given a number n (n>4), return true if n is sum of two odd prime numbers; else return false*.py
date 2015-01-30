# encoding=utf-8
# Given a number n (n>4), return true if n is sum of two odd prime numbers; else return false
'''
先求出 所有<n 的prime number, 然后再用 two sum做
'''

#如果是奇数比较好办。 因为prime只有2一个偶数。 只要check x-2是不是。
 # 偶数就暴力了。