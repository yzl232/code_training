# encoding=utf-8
'''
how to write a connection pool (i.e, a class that returns connections to the user, and if the user is done, returns them back to the pool)
'''

'''
This is about creating a Singlenton class that holds a cache of connections so that the connections can be reused when future requests to the database are required.

When you say that "When the user is done, returns them back to the pool" means that you just freed one of your N connection hold in your cache, wich means It can be use by another user/request/process/thread/etc

There is a creational design pattern called object pool pattern if you want to get into details.

Additionally, there are a lot open source software that are in charged of such task. In real life, It is hard that someones needs to rebuild the wheel, but It is a good idea to knoew in details such open source software to disscuss it during the interview and why not came up with your own implentation.
'''

'''
This is semaphore problem. Let say you have 20 connection pools, you will allow 20 threads to get the pool, and wait if there are more requests coming in. Until one of them returns it to the pool then the waiting thread can get it.
'''