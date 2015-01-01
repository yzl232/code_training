# encoding=utf-8
'''
How would you implement an infinite counter?
'''


'''
Use Linked List concept. Let us say that the maximum limit of an integer in the language is 65,536. Let us limit it to 9999.
The counter will increase from 0-9999. After that, add another node, with value 1 and change the first node value to 0. Do this infinitely by adding nodes whenever needed.
Thus, we can easily print the counter value.
'''


#意思就是本来是限制了范围的0~65536.   多个node。每个每个node最多存65535个数。 这就破去了限制。