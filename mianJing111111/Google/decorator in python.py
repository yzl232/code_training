# encoding=utf-8
'''

语法示例：

@dec1
@dec2
def test(arg):
    pass


其效果类似于
dec1(dec2(test(arg)))

其中dec1,  dec2返回的都是一个函数。
'''



def italic(fn):
    def wrap():
        return "<i>" + fn() + "</i>"
    return wrap

@italic
def hi():
    return "hello world"
print hi()