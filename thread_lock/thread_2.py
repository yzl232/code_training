__author__ = 'zhenglinyu'
import threading
import time
class timer(threading.Thread): #extends
    def __init__(self, no, interval):
        threading.Thread.__init__(self)
        self.no = no
        self.interval = interval
        self.stopFlag = False

    def run(self):  #override run method
        while not self.stopFlag:
            print 'Thread Object(%d), Time:%s\n' %(self.no, time.ctime())
            time.sleep(self.interval)

    def stop(self):
        self.stopFlag = True

def test():
    thread1 = timer(1, 1)
    thread2 = timer(2, 2)
    thread1.start()
    thread2.start()
    time.sleep(8)
    thread1.stop()
    thread2.stop()
    time.sleep(5)
    return

if __name__ == '__main__':
    test()