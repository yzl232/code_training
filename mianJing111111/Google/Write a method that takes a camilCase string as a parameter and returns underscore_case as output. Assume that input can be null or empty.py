# encoding=utf-8
'''
Write a method that takes a camilCase string as a parameter and returns underscore_case as output. Assume that input can be null or empty.

If CamilCase parametar starts with a capital letter turn it into lower case without puting underscore before it. How do you test this method ?
'''

#驼峰式命名
def camilCaseToUnderscore(a):
    if not a: return ''
    b =a.lower()
    c = zip(a, b)[1:]
    return  b[0]+''.join('_'+y if x!=y else y for x, y in c)

print camilCaseToUnderscore('iPhone')
print camilCaseToUnderscore('FirstName')