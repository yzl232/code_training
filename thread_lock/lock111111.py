__author__ = 'zhenglinyu'
import threading
import time
mylock = threading.RLock()   #Allocate a lock
num = 0  #Shared resource

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global num
        while True:
            mylock.acquire()
            print '\nThread: %s locked, Number = %d' %(self.t_name, num)
            if num>=4:
                mylock.release()
                print  '\nThread: %s released, Number = %d' %(self.t_name, num)
                break
            num+=1
            mylock.release()
            print '\nThread: %s released, Number = %d' %(self.t_name, num)

def test():
    thread1 = myThread('A')
    thread2 = myThread('B')
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    test()