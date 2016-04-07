'''
对，就是给一堆subnet mask，然后再给一些IP Address，然后拿这个IP Address去跟subnet mask比较，如果满足了某一个mask就return true。我给的方法是用一个trie把subnet都存起来，像prefix match一样去做
'''