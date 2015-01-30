# encoding=utf-8
'''
输出一堆photo, photo有文件名和时间, 输出是一堆album, 要给每个album命名名字, 最多100个photo, 然后分的时候, 要做到user-friendly. 这个面试官是个烙印, 我代码没写完. 大概的思路就是, 按照天数来分, 每个album的名字就是起止时间. 当然还有很多小细节, 比如一天的照片数可能大于100


印度人很恶心, 这个是个开放的题目, 没有固定的解法, 他想黑你很容易.
输入是一堆照片, 照片的就是一个class, 有时间和名字.
输出是一堆album, album也是一个class, 里面有名字和包含的照片(就是List<Photo>).

他说要求做到分出来的album能够user-friendly, 你怎么写他都可以说不达到要求. 当时他故意拖延我写代码的时间, 说我的分法不user-friendly.
你自己想想怎么写吧.


 album也要自己命名, 要求用户能够觉得这样命名make-sense.

'''

'''
Situation-Based Clustering
A solution that includes a means to roughly group pictures that are taken sequentially is proposed. Pictures are often grouped according to similar background scenery. The similar background scenery serves as a clue for the rough grouping of the pictures. With this rough grouping, people can see their pictures not only in time-order but also in groups with similar background properties.


或者用户自己用label。  user annotation

Face-Based Photo Search and Retrieval


#或者用名字来group。。  a~z
'''


class Photo:
    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time

class Solution:
    def arrange(photos):
        albums = [[] for i in range(26)]    #名字命名
        for x in photos:
            n = ord(x.name[0].lower()) - ord('a')
            albums[n].append(x)
        ret = []
        for y in albums:
            y.sort();  n = len(y)
            for i in range(n/100):  ret.append(y[i*100:i*100+100])
            if n%100!=0:  ret.append(y[n-n%100:])
        return ret

