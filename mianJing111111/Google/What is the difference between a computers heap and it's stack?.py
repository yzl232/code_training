# encoding=utf-8
'''
What is the difference between a computers heap and it's stack?
'''

#记忆： heap =》head+> 高。 为global

# heap  没有stack快。

'''
Physically stack and heap both are allocated on RAM and their implementation varies from language, compiler and run time

Stack is used for local variables of functions and to track function calling sequences.

Heap is used for allocating dynamically created variables using malloc, calloc or new.


Stack memory is freed whenever the function completes execution but the heap memory needs to be freed explicitly using delete, free or by garbage collector of the language.




Stack memory of a process is fixed size and heap is variable memory.



Stack is faster than heap as allocating memory on stack is simpler just moving stack pointer up.

In case of multi threading, each thread of process will have a different stack but all threads share single heap
'''