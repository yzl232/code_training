# encoding=utf-8
'''

简单的说就是代替get()
与以下两句等价


d.setdefault(5, 'A')

if 5 not in d:   cur[5] = {"A"}
cur = cur[5]
很不喜欢这个函数。 不直观。 一切都换成两句


#以后碰到可能不在dict里面的情况，就这样写。 非常好。
设置为0. 于是少了个else
if ch not in h:  h[ch]=0
h[ch]+=1

'''
d = {}
print d.setdefault(5, 'A')
print d
print d.setdefault(5, 'B')