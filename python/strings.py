# encoding=utf-8
'''

s = "Some things are immutable!"
s[-1] = "."
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment


'''

a = 'linux'
b = 'linux'
print a is b

a = 'a!'
b = 'a!'
print a is b
print a == b

a = "Baden!"
b = "Baden!"
print a is b


a = input("How old are you? ")
print a, type(a)
b = raw_input("How old are you?")
print b, type(b)