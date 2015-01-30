# encoding=utf-8
'''
Given set amount of memory and ram, how do you implement a process that
takes the longest amount of time to finish? The process has to finish, it
can not be an infinite loop. (Of all of the questions I got asked from
Google, I'm not sure I know the right answer to this one to this day)
'''

'''
假设有一台迷你计算机，1KB的内存，1MHZ的cpu，已知该计算机执行的程序可出现确定
性终止（非死循环），问如何求得这台计算机上程序运行的 最长时间，可以做出任何
大胆的假设。

分析：任何时候内存状态都不能相同，否则进入死循环：假设某2个时刻t1,t2满足t1小
于t2，内存的状态完全相同，那么到达t2时刻又想当于回到了t1的执行位置。1k的内存
共有状态 2^(1024*8)个（相当大）每秒cpu为1m，一秒钟改变1m次，所以两者相除即可
得CPU的最长运行时...
'''


'''
Thank you. The answer I gave during the interview is to clear all memory and
treat it like a big number. I increment by 1 per cpu cycle. I was never
able to provide a good enough argument for why this is the slowest possible
program. I like your explanation. It is impossible to prevent an infinite
loop if memory got into the same state without terminating.
'''