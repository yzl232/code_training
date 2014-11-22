# encoding=utf-8
def ifib(n):
    '''return fibinochi'''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print ifib.__doc__

'''
. An asterisk "*" is used in front of the last parameter name to denote it as a tuple reference. This asterisk shouldn't be mistaken with the C syntax, where this notation is connected with pointers.
'''



# which can take an arbitrary number of arguments.

#*的好处是可以使任意多的arguments
def arbitrary(x, y, *more):
    print "x=", x, ", x=", y
    print "arbitrary: ", more

print arbitrary(3,4)

print arbitrary(3,4, "Hello World", 3 ,4)
#x and y are regular positional parameters in the previous function. *more is a tuple reference.


def ref_demo(x):
    print "x=",x," id=",id(x)
    x=42
    print "x=",x," id=",id(x)

ref_demo(5)





def locations(city, *other_cities): print(city, other_cities)
locations("Paris", "Strasbourg", "Lyon", "Dijon", "Bordeaux", "Marseille")
locations("Paris")


def arithmetic_mean(x, *l):
    """ The function calculates the arithmetic mean of a non-empty
        arbitrary number of numbers """
    sum = x
    for i in l:
        sum += i

    return sum / (1.0 + len(l))

print arithmetic_mean(4,7,9)
print arithmetic_mean(4,7,9,45,-3.7,99)

'''
This works fine, but there is a catch. What if somebody wants to call the function with a list, instead of a variable number of numbers, as we have shown above? We can see in the following, that we raise an error, as most hopefully, you might expect:

>>> l = [4,7,9,45,-3.7,99]
>>> arithmetic_mean(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "statistics.py", line 8, in arithmetic_mean
    return sum / (1.0 + len(l))
TypeError: unsupported operand type(s) for /: 'list' and 'float'

The rescue is using another asterisk:

>>> arithmetic_mean(*l)
26.71666666666667
>>>

'''
l = [4,7,9,45,-3.7,99]
print arithmetic_mean(*l)


def f(x, y, z):  return (x, y, z)
p = (1, 2, 5)
print f(*p)


'''
Arbitrary Keyword Parameters
There is also a mechanism for an arbitrary number of keyword parameters. To do this, we use the double asterisk "**" notation:

>>> def f(**args):
...     print(args)
...
>>> f()
{}
>>> f(de="Germnan",en="English",fr="French")
{'fr': 'French', 'de': 'Germnan', 'en': 'English'}
>>>

Double Asterisk in Function Calls
The following example demonstrates the usage of ** in a function call:

>>> def f(a,b,x,y):
...     print(a,b,x,y)
...
>>> d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
>>> f(**d)
('append', 'block', 'extract', 'yes')

and now in combination with *:

>>> t = (47,11)
>>> d = {'x':'extract','y':'yes'}
>>> f(*t, **d)
(47, 11, 'extract', 'yes')
>>>

'''


def f1(a,b,x,y):
    print (a, b, x, y)

t = (47,11)
d = {'x':'extract','y':'yes'}
f1(*t, **d)
f1(** {'a':'append', 'b':'block','x':'extract','y':'yes'})
ddd =  {'a':'append', 'b':'block','x':'extract','y':'yes'}
f1(**ddd)


def abs(**a): print a
abs(de="Germnan",en="English",fr="French")

def varpafu(*x): return x
print varpafu()
print varpafu(34,"Do you like Python?", "Of course", "23ehr2ih293r82hf2i3h23h2")


'''
There is also a mechanism for an arbitrary number of keyword parameters. To do this, we use the double asterisk "**" notation:

无限多个默认传值。

所以说  def abs(**a): print a
 而是默认传值de="Germnan",en="English",fr="French"
 **传入a=3,  变成一个dict
 *传入3， 4， 5， 变成一个tuple


'''


