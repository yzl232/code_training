# encoding=utf-8
def f1():
    return 1
def f2():
    return 2
myfuctions = {'a':f1, 'b':f2}
print myfuctions['a']()
print myfuctions['b']()
'''
每个函数都是变量


closures and currying
'''

def outer(outArg):
    def inner(innerArg):
        return outArg+innerArg
    return outArg

func = outer(10)

def make_adder(addend):
    def adder(augend):
        return augend + addend
    return adder   #返回的是函数。
#我们可以把addend看做新函数的一个配置信息,配置信息不同,函数的功能就不一样了,也就是能得到定制之后的函数.


p = make_adder(23)
q = make_adder(44)
print p
print q
print p(100)
print q(100)



def hellocounter (name):
    count=[0]
    def counter():
        count[0]+=1
        print 'Hello,',name,',',str(count[0])+' access!'
    return counter

hello = hellocounter('ma6174')
hello()
hello()
hello()
'''
这个程序比较有趣,我们可以把这个程序看做统计一个函数调用次数的函数.count[0]可以看做一个计数器,没执行一次hello函数,count[0]的值就加1。也许你会有疑问:为什么不直接写count而用一个列表?这是python2的一个bug,如果不用列表的话,会报这样一个错误:

UnboundLocalError: local variable 'count' referenced before assignment.

什么意思?就是说conut这个变量你没有定义就直接引用了,我不知道这是个什么东西,程序就崩溃了.于是,再python3里面,引入了一个关键字:nonlocal,这个关键字是干什么的?就是告诉python程序,我的这个count变量是再外部定义的,你去外面找吧.然后python就去外层函数找,然后就找到了count=0这个定义和赋值,程序就能正常执行
'''




def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello()



'''


decorator


怎么样?这个程序熟悉吗?这不是传说的的装饰器吗?对,这就是装饰器,其实,装饰器就是一种闭包,我们再回想一下装饰器的概念:对函数(参数,返回值等)进行加工处理,生成一个功能增强版的一个函数。再看看闭包的概念,这个增强版的函数不就是我们配置之后的函数吗?区别在于,装饰器的参数是一个函数或类,专门对类或函数进行加工处理。

python里面的好多高级功能，比如装饰器，生成器，列表推到，闭包，匿名函数等，开发中用一下，可能会达到事半功倍的效果！



语法示例：

@dec1
@dec2
def test(arg):
    pass


其效果类似于
dec1(dec2(test(arg)))
'''