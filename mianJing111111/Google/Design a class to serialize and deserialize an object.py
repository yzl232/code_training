# encoding=utf-8

'''
Design a class to serialize and deserialize an object



http://stackoverflow.com/questions/8586511/serialization-deserialization-mechanism

http://www.javaworld.com/article/2072752/the-java-serialization-algorithm-revealed.html



The default involves a hashcode. Serialization creates a single hashcode, of type long, from the following information:

    The class name and modifiers

    The names of any interfaces the class implements

    Descriptions of all methods and constructors except private methods and constructors

    Descriptions of all fields except private, static, and private transient

    这个讲的好。
http://www.cnblogs.com/redcreen/articles/1955307.html
'''