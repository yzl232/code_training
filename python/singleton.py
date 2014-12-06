class Singleton(object):
    def __new__(cls, *args, **kw):  #override new
        if not hasattr(cls, '_instance'):  cls._instance = object.__new__(cls, *args, **kw)  #call the original __new__ method
        return cls._instance

class a:
    pass
s = a()
print type(s)