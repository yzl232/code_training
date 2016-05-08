# encoding=utf-8
'''
What is the difference between a computers heap and it's stack?
'''


#看看下面这个stack overflow就理解了.
'''
You can cause a stack overflow quite easily in python, as in any other language, by building an infinately recursive funcion. This is easier in python as it doesn't actually have to do anything at all other than be recursive.

>>> def foo():
...     return foo()
...

>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  .......
  File "<stdin>", line 2, in foo
RuntimeError: maximum recursion depth exceeded
>>>

As for the heap, that is managed by a garbage collector. You can allocate lots of objects and eventually run out of heap space and Python will raise a MemoryError, but it's going to take a fair amount of time. You actually did that with your 'stack overflow' example in the question. You stored a reference to a string on the stack, this string took up all the free memory available to the process. As a rule of thumb, Python stores a reference to a heap structure on the stack for any value that it can't guarantee the size of.



Physically stack and heap both are allocated on RAM and their implementation varies from language, compiler and run time

Stack is used for local variables of functions and to track function calling sequences. (考虑recursion无限循环 ,用的stack)

Heap is used for allocating dynamically created variables using malloc, calloc or new.


Stack memory is freed whenever the function completes execution.

 but the heap memory needs to be freed explicitly using delete, free or by garbage collector of the language.




Stack memory of a process is fixed size and

heap is variable memory.



Stack is faster than heap as allocating memory on stack is simpler just moving stack pointer up.

In case of multi threading, each thread of process will have a different stack but all threads share single heap




'''