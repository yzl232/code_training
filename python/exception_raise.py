# encoding=utf-8
'''


    "How do I manually throw/raise an exception in python?"

Short Answer:

Use the most specific Exception constructor that semantically fits your issue.

Be specific in your message.


'''


raise ValueError('A very specific bad thing happened', 'foo', 'bar', 'baz')


