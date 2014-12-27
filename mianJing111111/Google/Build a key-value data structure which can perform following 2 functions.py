# encoding=utf-8
'''
Build a key-value data structure which can perform following 2 functions
- lookup
- rangeLookup(key1, key2)
'''


'''
We can implement it by using a combination of HashMap and BST. HashMap will contain entry for key-value pair and BST only keys. All keys will be maintained in BST (sorted order).

lookup(Key): Make a simple lookup in to HashMap
rangeLookup() - It will be in two parts -
Keys[] rage(Key1, Key 2) from BST
Entry[] lookups(Keys[]) in HashMap


Since lookup is the major concern here, BSTs are the best
'''