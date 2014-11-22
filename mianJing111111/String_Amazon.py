# encoding=utf-8
#http://www.mitbbs.com/article_t/JobHunting/32633319.html
'''
有一种String,是把一个更短的String重复n次而构成的，那个更短的String长度至少为
2，输入一个String写代码返回T或者F
例子：
"abcabcabc"  Ture   因为它把abc重复3次构成
"bcdbcdbcde" False  最后一个是bcde
"abcdabcd"   True   因为它是abcd重复2次构成
"xyz"       False  因为它不是某一个String重复
"aaaaaaaaaa"  False  重复的短String长度应至少为2（这里不能看做aa重复5次)

要求算法复杂度为O(n)

'''
def isMultiple(string):
    if not string:   return
    step = 2
    repeatstring = None
    while step < len(string):
        pat = string[:step]
        if len(string) % len(pat) == 0:
            if pat*(len(string)/len(pat)) == string:
                if not repeatstring:
                    repeatstring = pat
        step += 1
    if repeatstring:
        print 'repeatstring:', repeatstring
        return len(set(repeatstring)) != 1
    else:     return False

print  isMultiple("abaaba")
print  isMultiple("abcabcabc")
print  isMultiple("abaaba")
print  isMultiple("xyz")
print isMultiple("aaaaaaaaaa")