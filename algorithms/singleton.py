class Singleton(object):
    def __new__(cls, *args, **kw):  #override new
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)  #cls : class
            cls._instance = orig.__new__(cls, *args, **kw)  #call the original __new__ method
        return cls._instance

class a:
    pass
s = a()
print type(s)