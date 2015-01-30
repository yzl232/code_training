# encoding=utf-8
'''
还一个是设计题：假设有许多geographically distributed servers，用户可以向这些server request a ID。要求：1、ID必须globally unique；2、ID的ordering需要尽可能的反映现实时间；3、效率。

这种题思路应该从tradeoff上走，可以从极端例子来考虑。那时太年轻，虽然说出几种方案但没有用tradeoff的思路，不能李菊福，哎。
'''

# 时间戳___机器id____每秒内的

#最底下贴了那道类似的题目。
# str(time)+ str(id)
# 时间不一样时。  id重置。

# 或者加上mac address.  ()



#从哈佛课上得笔记 .  解法1 shared storage  解法2： cookies
## .  单独用一个machine放database。  每个server都向这个machine要ID。     （这个机器 kind of  'global',  each machine will look up this one.）
#于是适合第一种
#重点是画好图。。

'''
比如n台机器  我们可以用时间戳___机器id____每秒内的count     连接的形式 时间戳可以采取年月日时分秒，
'''

'''


As for Facebook, Google, etc: The database servers are not all in one location and certainly not all in total sync all the time. They all employ a distributed system over several clusters of servers for different geographical areas.

Clusters are distributed in many countries. Frequency of updates between clusters depends on the need of the system to acceptably work.

If you take Facebook e.g: Most of the time you communicate with friends in your own country.

So keeping servers in your country will have an immediate effect and your friends will instantly see your messages.

按国家分

Friends in other contries might have a delay, depending on how often the clustered server nodes are updated. IIRC Facebook clusters interact by requesting information from other clusters if needed. Many times have I gotten a message saying something like "This user updated status to blah blah". When clicking the link to the whole message I've gotten an error message. This is a syncronization problem between the clusters. Some information have been synchronized while other have not.

How you build the infrastructure depends on how many users, how often the data needs to be synchronized, etc.

Another example, Email: The Email system is a distributed system across the whole planet. A server with a single user is not that busy compared to a server with 1 million users. How would you solve the delivery issues for a busy server? More distributed local server? More powerful servers? More powerful internet connection? All of the above? Since the underlying concept of email (to deliver messages from one node to another) doesn't change regardless of the number of Email users, you'll need to design you particular system to accommodate for all your users. Regardless of how you design your system there are times when emails are delayed in delivery because there simply is too much traffic on the other nodes in the chain.

The same concept applies to Facebook. They design and build their farms for a specific region but the whole system relies on "geographical differences". That is, you are more likely to interact with users in your own region than other regions.

As for your particular problem: It all depends on how many users there are.
A single database server (or clustered server) might work for you. If there is need for distributed clustered server farms then you might have to write your own system for syncronization like Facebook and Google did. This solution depends on what your users need and how the system is intended to work. I don't know of any standardized system that is a "works for all" solution.

I've been ranting a lot here and it's quite late and I might be totally off target but hey, it's my 2 cents.

Cheers!

'''





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
