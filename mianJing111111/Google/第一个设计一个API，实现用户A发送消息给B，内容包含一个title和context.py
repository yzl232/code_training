# encoding=utf-8
# 第一个设计一个API，实现用户A发送消息给B，内容包含一个title和context

class User:
    def __init__(self, id):
        self.id = id
        self.s = []
    def send(self, id2, text, title):
        pass

'''
第一个设计一个API，实现用户A发送消息给B，内容包含一个title和context
不知道考点是啥= =
我说 bool send_message(string A, string B, string title, string context) {}
面试官问如果调用这个函数的人把参数的顺序搞错了怎么办，我说那把参数封装成一个class，问我python里面应该怎么做，没答上来。。

'''