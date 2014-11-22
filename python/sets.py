# encoding=utf-8

'''

Immutable Sets
Sets are implemented in a way, which doesn't allow mutable objects. The following example demonstrates, that we cannot include for example lists as elements:

cities = set((("Python","Perl"), ("Paris", "Berlin", "London")))
cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
'''

print set("A Python Tutorial")



cities = frozenset(["Frankfurt", "Basel","Freiburg"])
#Frozensets are like sets except, that they cannot be changed, i.e. they are immutable:
'''
>>> cities.add("Strasbourg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
'''

'''
We can define sets (since Python2.6) without using the built-in set function. We can use curly braces instead:

>>> adjectives = {"cheap","expensive","inexpensive","economical"}
>>> adjectives
set(['inexpensive', 'cheap', 'expensive', 'economical'])
>>>


'''

print {4, 5, 7}
