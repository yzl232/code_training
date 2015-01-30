# encoding=utf-8
'''
How do you make sure an API does not leak memory?
'''

# 比如hashtable之类。 不用的话， 删除。
#Creating a memory leak with Java

'''
Java内存泄露的原因

1、静态集合类像HashMap、Vector等的使用最容易出现内存泄露，这些静态变量的生命周期和应用程序一致，所有的对象Object也不能被释放，因为他们也将一直被Vector等应用着。

2、内部类和外部类的引用容易出现内存泄露的问题

3、监听器的使用，java中往往会使用到监听器，在释放对象的同时没有相应删除监听器的时候也可能导致内存泄露。

4、大量临时变量的使用，没有及时将对象设置为null也可能导致内存的泄露

5、数据库的连接没有关闭情况，包括连接池方法连接数据库，如果没有关闭ResultSet等也都可能出现内存泄露的问题。





举例一个内存泄露的例子：






别以为o对象被回收了，实际上v引用了这些对象，还被引用的对象GC是没有办法回收的，这样就很可能导致内存的泄露。

哪里分析错或者需要补充的地方，希望得到指点，谢谢
'''
class Cal:
    d = {}
    def sqr(self, i):
        ret = i*i
        self.d[i] = ret
        return ret
s = Cal()
print s.sqr(5)

#我们没有用到d。
#自创一个memory leak


'''

Well I guess there are couple of ways we can approach this

1> Design API such that it only Process the functionality and no memory allocation within it.
2> Use the Smart pointer concept for every pointer usage within the API.
3> Can make API's so that for every allocation there must be the deallocation called in. for every condition.


'''



'''
As the author of the API, we ensure no memory leak by
1. making object ownerships clear.
2. protecting heap allocation with smart pointers.
3. output arguments should be provided from caller or use sharedptr.
As a user of the API, we can do some test.
1. use tools with memory leak detection, i.e. valgrind.
2. limit the heap memory of the program and simply try to amplify possible memory leak by repeatedbly calling the API.
'''