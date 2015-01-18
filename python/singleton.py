# encoding=utf-8


class Singleton(object):
    def __new__(cls, *args, **kw):  #override new
        if not hasattr(cls, '_instance'):  cls._instance = object.__new__(cls, *args, **kw)  #call the original __new__ method
        return cls._instance

#原理很简单，就是更改new方法。 如果已经有了instance。略去。 不然新建instance

class MyClass(Singleton):
    a = 1

one = MyClass()
print one.a
two = MyClass()

two.a = 3
print one.a