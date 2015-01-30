# encoding=utf-8
'''
design a system to return an unique ID for each request. For most of requests, the ID value should increase as time goes, the system should handle 1000 requests per second at least.
timestamps alone is not valid since there might be multiple requests with same timestamps.
'''
#好像有很多不错的解释
'''
http://www.careercup.com/question?id=5169800024162304
'''


# http://blog.tompawlak.org/generate-unique-identifier-nodejs-javascript
# 上面的链接比较好

# str(time)+ str(id)
# 时间不一样时。  id重置。

# 或者加上mac address


# UUIDs may be generated from a combination of system time stamp, CPU / system unique ID, NIC MAC addresses, HBA WWNs etc.
'''
Let's assume the following parameters:
What's the min length of the ID? <= 128 bits
In that case I'll choose the standard 128 bit UUID format.
The requirement states the system should handle 1000 request/s at least.
What's the average request rate? 1000 < avg req. rate < 10,000
What's the max. burst rate the system must handle? < 1,000,000
What's the max. latency (wait time) for a request? 1 ms
'''


'''
The problem of generating unique IDs has been solved. All modern OS'es have that functionality built in. (And many embedded/mobile OS'es provide API's as well.)
And if asked: UUIDs may be generated from a combination of system time stamp, CPU / system unique ID, NIC MAC addresses, HBA WWNs etc.
The problem is how to serve lots of such IDs however generated.
Questions to ask:
What's the min length of the ID?
The requirement states the system should handle 1000 request/s at least.
What's the average request rate?
What's the max. burst rate the system must handle?
What's the max. latency (wait time) for a request?



#生产者。 消费者问题。

It's a classical consumer-producer problem.
In this case we have many consumers of UUIDs and one producer.
All common server OS'es have API's to create UUIDs. For embedded/mobile systems one may have to build the functions. Let's assume the OS provides an API to generate UUIDs and the max. running time of the API is 1ms.
First Pre-allocate 2 Mio UUIDs into an array / stack/ heap (depending on implementation) structure.
2 Mio UUIDs ensures system can handle burst rate.
(If no overhead 2 Mio UUIDs would take ~ 32MB of RAM)
Again, not a problem on today's server system with many GB of RAM, but may be a problem on an embedded system.)
The solution needs to ensure that its pool of UUIDs doesn't run out as consumers request them and they are replenished.
'''


'''
This question is quite open-ended.

For starter, how about appending unique numbers to the timestamp?  If each server has an ID we can also include it to further reduce collisions.

If IDs must be unique, then I suppose you can design a counter that will return an ID and increment it at the same time. You will then need mutex to access this counter.
'''
