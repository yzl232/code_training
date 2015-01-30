# encoding=utf-8
'''
假设用以下class来代表file:

    class File {
        void delete();
        bool isDir();
    };

复制代码
给你一个File，然后删除它。Post-order traverse。后来还问了如果是在os中实现，应该如何lock。

'''
import threading
myLock = threading.RLock()
#肯定用recursion的。 递归调用delete
class File:
    def __init__(self):
        self.contents = None
        global myLock

    def isDir(self):
        pass

    def delete(self):
        myLock.acquire()
        if self.isDir():  #注意先后     Post-order traverse
            for e in self.contents:  e.delete()
        del self
        myLock.release()