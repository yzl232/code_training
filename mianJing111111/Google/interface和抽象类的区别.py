# encoding=utf-8
#interface和抽象类的区别



'''
In .NET (similar for Java):

    interfaces can have no state or implementation
    a class that implements an interface must provide an implementation of all the methods of that interface
    abstract classes may contain state (data members) and/or implementation (methods)
    abstract classes can be inherited without implementing the abstract methods (though such a derived class is abstract itself)
    interfaces may be multiple-inherited, abstract classes may not (this is probably the key concrete reason for interfaces to exist separately from abtract classes - they permit an implementation of multiple inheritance that removes many of the problems of general MI).

'''