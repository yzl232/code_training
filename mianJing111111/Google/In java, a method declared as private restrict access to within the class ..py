# encoding=utf-8
'''
In java, a method declared as private restrict access to within the class
. For example, a private void doHeartbeat() method within Heartbeat class
can only be called within the Heartbeat class. However, it doesn't prevent
the Heartbeat class to access the method of a different Heartbeat object.
For example, a private void forceHeartbeat(Heartbeat other) method is
allowed to call other.doHeartbeat(). Java doesn't provide a way to limit
access to a per object level. Why not?
'''

# 2个time。 一个是 compile time .  一个是runtime>      compile time施加access restriction.   runtime才run  method。  顺序在后面。  如果在runtime check。 too costly
'''
In java, access restriction is enforced during compilation time.

If a class try to access the private method of a different class, it wouldn't compile.
On the other hand, objects are created during runtime.



In order to properly
perform object level access restriction, java will have to check access
restrictions during runtime on everything method call. This is too costly.
'''