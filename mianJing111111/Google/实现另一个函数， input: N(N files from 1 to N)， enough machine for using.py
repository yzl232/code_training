# encoding=utf-8
'''

给个函数
long sum(int fileId, int machID){
    //return the sum of the numbers in this file using this machine.
}

实现另一个函数，
input: N(N files from 1 to N)， enough machine for using
output; the total sum of these files.

long getAllSum(int N){



}



'''
#  没觉得是多线程，都有machineid了，怎么是多线程？分布式吧。map reduce

'''

同一个machine多线程的话，blockingQueue里面放fileId，sum设为static的
atomicInteger
多个machine的话，就是IPC，



一个machine做coordinator，往message queue里面放
fileID。其他machine从message queue里面拿fileID，统计完把结果放到另外一个
message queue里面，coordinator取出结果然后sumAll.

其实就是mapper + reducer
'''

#一个global machine
#
'''

mapper:
for file in files:
    print fileID, sum


reducer:
sum of all

......



'''