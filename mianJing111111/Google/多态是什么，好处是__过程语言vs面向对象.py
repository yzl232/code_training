# encoding=utf-8
'''
过程语言vs面向对象

 3.过程语言vs面向对象 介绍下区别。
 4.多态是什么，好处是？
 5.4种修饰符，如何使用？
 6.private 机制
 7.java 传值还是引用？
'''

# ，接口的多种不同的实现方式即为多态。
# present the same interface for differing underlying forms (data types).
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]

for animal in animals:
    print animal.name + ': ' + animal.talk()



'''
把不同的子类对象都当作父类来看，可以屏蔽不同子类对象之间的差异，写出通用的代码，做出通用的编程，以适应需求的不断变化。
'''


'''
 10 down vote accepted


The primary benefit of polymorphism is freedom.

When an object has a reference to another, it can invoke methods on that object reference without knowing, or caring, what the implementation is.

So it allows you to make the powerful statement: Don't know, don't care.
'''

#  an interface may have multiple different implementations

# OOP vs Functional Programming vs Procedural

'''
n a purely procedural style, data tends to be highly decoupled from the functions that operate on it.

In an object oriented style, data tends to carry with it a collection of functions.

In a functional style, function is a data type.
Algorithms tend also to be defined in terms of recursion and composition rather than loops and iteration.
'''
