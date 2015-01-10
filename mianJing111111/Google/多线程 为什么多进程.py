# encoding=utf-8
#多线程
# 为什么多进程
'''
Both processes and threads are independent sequences of execution. The typical difference is that threads (of the same process) run in a shared memory space, while processes run in separate memory spaces.


主要2点。 见GT的笔记
1     进程更大。  一个process可以有多个thread
2     进程独立的资源。  thread  share 资源



还有一点。
thread,  process  使用global的 heap.
自己的stack。   heap==head在头上。 共有
'''