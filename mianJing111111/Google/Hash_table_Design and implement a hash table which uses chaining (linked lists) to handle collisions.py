# encoding=utf-8
'''
Design and implement a hash table which uses chaining (linked lists) to handle collisions


下面这个不是用chain解决冲突。 是用[]解决冲突。


'''
#G家考过好几次


MAX_SIZE = 15

class Hash1:
    def __init__(self, items = [[] for i in range(MAX_SIZE)]):
        self.items = items
    
    def hashCodeOfKey(self, key):
        return len(str(key)) % len(self.items) 
    
    def put(self, key, value):
        x = self.hashCodeOfKey(key)
        if len(self.items[x]) == 0: 
            self.items[x].append((key, value))
        else:
            if (key, value) in self.items[x]:
                self.items[x].remove((key, value))
            self.items[x].append((key, value))
    
    def get(self, key):
        x = self.hashCodeOfKey(key)
        if len(self.items[x]) == 0: return 
        for c in self.items[x]:
            if c[0] == key:
                return c[1]
        return 

'''
下面用chain  linkedlist
'''
    

MAX_SIZE = 15

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class Hash2:
    def __init__(self, items = [None for i in range(MAX_SIZE)]):
        self.items = items

    def hashCodeOfKey(self, key):
        return len(str(key)) % len(self.items)

    def put(self, key, value):
        x = self.hashCodeOfKey(key)
        if not self.items[x]:
            self.items[x] = ListNode(key, value)
        else:
            dummy = ListNode(0); cur = self.items[x];  dummy.next = cur
            pre = dummy
            while cur:
                if cur.key == key:
                    pre.next = cur.next
                pre, cur = cur, cur.next
            cur.next = ListNode(key, value)
            self.items[x] = dummy.next

    def get(self, key):
        x = self.hashCodeOfKey(key)
        if not self.items[x] : return
        val = None
        cur = self.items[x]
        while cur:
            if cur.key == key:
                val = cur.val
        return val

        
    