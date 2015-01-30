# encoding=utf-8
'''
Give efficient implementation of the following problem.

An item consist of different keys say k1, k2, k3. User can insert any number of items in database, search for item using any key, delete it using any key and iterate through all the items in sorted order using any key. Give the most efficient way such that it supports insertion, search based on a key, iteration and deletion.
'''

#3种key。 要可以三种iterator。 可以使用任意key来  search, delete

'''
Solution

There’re 3 keys, so we need 3 maps to store search map for 3 types of keys. For example, the DS is like this:

    (date, name, country) –> ItemObject

Then we would have:

    date –> a list of ItemObject

    name –> a list of ItemObject

    country –> a list of ItemObject

Since we need to iterate in order, we choose ordered dict over HashMap.

For scalability purpose, we use another HashMap<KeyType, ordered dict> and put 3 items in.
Final Data Structure


主要的数据是存在double linked list。 另外两个都是存了pointer to the DLL node
3 DS needed. source

    DoubleLinkedList
    Ordered Dict<KeyValue, List> index;
    HashMap<KeyType, ordered dict<KeyValue, List>> mapOfIndexes;
    hashmap: 三种类key，对应 三种ordered  dict

Method add(item): void   O(1)

    add node in DoubleLinkedList.   tail.  O(1)
    For each key, get ordered dict from HashMap and add node into ordered dict.

Method search(key): List   O(1)

    Get ordered dict from HashMap for provided key.
    Look up from the ordered dict
    Return item

Method delete(key): List      O(1)

    Using search method get List Of item
    Delete items from ArrayList and also delete its mapping from all (3) ordered dict

Method orderedIterator(keytype): Iterator

    Get ordered dict from HashMap for provided key
    iterate using the ordered dict.

'''


# ordered dict我记得做不到O(1)  。  排序的话用bst吧 O(logN)