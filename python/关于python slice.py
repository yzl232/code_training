# encoding=utf-8
a = [1, 3, 2]
b = a[1:3]
print a, b
print id(a[-1])
print id(b[-1])
b[1]=1
print id(a[-1])
print id(b[-1])

# 可以看出。 用了slice,是一种shallow copy.   a, b是独立的。 但是如果你不改变b的话， 也没有消费新的空间。
# 也就是说。
# a[1:3] == b[:].  并没有开辟新的空间。
#因为python 很 smart.
#所以可以放心使用。