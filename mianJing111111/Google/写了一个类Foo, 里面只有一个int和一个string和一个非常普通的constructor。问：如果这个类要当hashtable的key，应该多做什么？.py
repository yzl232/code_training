# encoding=utf-8
'''
写了一个类Foo, 里面只有一个int和一个string和一个非常普通的constructor。问：如果这个类要当hashtable的key，应该多做什么？
'''

'''

All classes that have instances used as keys in a hash-like data structure must correctly implement the equals and hashCode methods.


目前综合起来比较正确的答案是： 写好equals函数，然后，override hashcode提供比较靠谱的hash function。
他还问我这个hashcode的好坏应该有什么判别标准，答：尽可能地避免conflict
'''