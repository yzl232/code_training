# encoding=utf-8
# 用同样的代码同样的数据跑测试，为啥结果会不一样，有两种可能

# 1   random variable,      time variable ,  user input
'''
You are given the source to an application which crashes when it is run. After running it ten times in a debugger, you find it never crashes in the same place. The application is single threaded, and uses only the C standard library. What programming errors could be causing this crash? How would you test each one?
'''


# random,  time variable


'''

 2. Memory Leak: The program may have run out of memory

 . Other culprits are totally random for each run since it depends on the number of processes running at that particular time.

 This also includes heap overflow or corruption of data on the stack.


It is also possible that the program depends on another application / external module that could lead to the crash.

If our application, for example, depends on some system attributes and they are modified by another program,

 then this interference may lead to a crash. Pro- grams which interact with hardware are more prone to these errors.
'''