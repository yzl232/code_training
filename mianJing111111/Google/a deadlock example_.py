# encoding=utf-8
#提供一个一定会死锁的一个代码
import  threading
l1 = threading.RLock()
l2 = threading.RLock()
# thread 1
while True:
    l1.acquire()
    l2.acquire()
    pass
    l2.release()
    l1.release()


#thread 2
while True:
    l2.acquire()
    l1.acquire()
    pass
    l1.release()
    l2.release()
'''
Suppose thread 1 is running and locks M1, but before it can lock M2, it is interrupted. Thread 2 starts running; it locks M2, when it tries to obtain and lock M1, it is blocked because M1 is already locked (by thread 1). Eventually thread 1 starts running again, and it tries to obtain and lock M2, but it is blocked because M2 is already locked by thread 2. Both threads are blocked; each is waiting for an event which will never occur.
'''