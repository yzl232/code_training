# encoding=utf-8
'''
第二题是有这么一个class Contact，里面有一个String的name，和一个List<String>
装着email address，是这个Contact有的address，用一个list装着是因为一个人有可
能有多个email，现在给你an array of Contact，比如
#1 John [john@gmail.com]
#2 Mary [mary@gmail.com]
#3 John [john@yahoo.com]
#4 John [john@gmail.com, john@yahoo.com, john@hotmail.com]
#5 Bob [bob@gmail.com]
现在我们知道如果email address相同的话，那么就说明是同一个人，现在要做的是根
据这些email address，把同一个contact给group起来，生成一个List<List<Contact>>
，比如我们就可以知道#1，#3，#4是同一个人。注意不能根据名字来group，因为有可
能有相同名字的人，或者同一个人有可能有不同的名字来注册之类的。我给出了一个类
似graph的解法。时间不够，就没有写code，只是把逻辑解释了一遍。
'''
# name完全没有用上
#比较tricky。 用hash。  key: email.    val:  自己建立id.
class Solution: #自己建立2个hashmap。 一个email-myid,   一个是myid- [email1, email2, ...]
    def sanitizeContacts(self, contacts):
        id = 0; emailToid={};  idToEmail={}  #d1 key 是email。val是id
        for c in contacts:   #d2 key 是 id , val 是emails
            myId = -1 #起了flag的作用
            for email in c[1]: #第一遍找有没有存在
                if email in emailToid:  myId=emailToid[email]    #found group
            if myId<0:
                id+=1
                myId=id
                idToEmail[myId] = set()
            for email in c[1]:  #主要在第二遍赋值
                emailToid[email]=myId
                idToEmail[myId].add(email)
        return idToEmail
snapchat也有考
东欧大叔，project diving deep, 题目是手机上的通讯录，每条记录只有(name, number)这种pair,有些记录名字重复，有些记录号码重复，让我返回一个list<list<Record>>，将所有记录按人分组。比较tricky的点在于(ABC,123), (ABC, 456), (BCD, 456)三条记录，第一条和第三条也属于同一个人。要求时间复杂度尽量小。
'''