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



    AC ED: STREAM_MAGIC. 声明使用了序列化协议.
    00 05: STREAM_VERSION. 序列化协议版本.
    0x73: TC_OBJECT. 声明这是一个新的对象.

    0x72: TC_CLASSDESC. 声明这里开始一个新Class。
    00 0A: Class名字的长度.
    53 65 72 69 61 6c 54 65 73 74: SerialTest,Class类名.
    05 52 81 5A AC 66 02 F6: SerialVersionUID, 序列化ID，如果没有指定，
    则会由算法随机生成一个8byte的ID.
    0x02: 标记号. 该值声明该对象支持序列化。
    00 02: 该类所包含的域个数。

    0x49: 域类型. 49 代表"I", 也就是Int.
    00 07: 域名字的长度.
    76 65 72 73 69 6F 6E: version,域名字描述.

    0x4C: 域的类型.
    00 03: 域名字长度.
    63 6F 6E: 域名字描述，con
    0x74: TC_STRING. 代表一个new String.用String来引用对象。
    00 09: 该String长度.
    4C 63 6F 6E 74 61 69 6E 3B: Lcontain;, JVM的标准对象签名表示法.
    0x78: TC_ENDBLOCKDATA,对象数据块结束的标志

    0x72: TC_CLASSDESC. 声明这个是个新类.
    00 06: 类名长度.
    70 61 72 65 6E 74: parent,类名描述。
    0E DB D2 BD 85 EE 63 7A: SerialVersionUID, 序列化ID.
    0x02: 标记号. 该值声明该对象支持序列化.
    00 01: 类中域的个数.

    0x49: 域类型. 49 代表"I", 也就是Int.
    00 0D: 域名字长度.
    70 61 72 65 6E 74 56 65 72 73 69 6F 6E: parentVersion，域名字描述。
    0x78: TC_ENDBLOCKDATA,对象块结束的标志。
    0x70: TC_NULL, 说明没有其他超类的标志。.

    00 00 00 0A: 10, parentVersion域的值.

    00 00 00 42: 66, version域的值.

    0x73: TC_OBJECT, 声明这是一个新的对象.
    0x72: TC_CLASSDESC声明这里开始一个新Class.
    00 07: 类名的长度.
    63 6F 6E 74 61 69 6E: contain,类名描述.
    FC BB E6 0E FB CB 60 C7: SerialVersionUID, 序列化ID.
    0x02: Various flags. 标记号. 该值声明该对象支持序列化
    00 01: 类内的域个数。

    0x49: 域类型. 49 代表"I", 也就是Int..
    00 0E: 域名字长度.
    63 6F 6E 74 61 69 6E 56 65 72 73 69 6F 6E: containVersion, 域名字描述.
    0x78: TC_ENDBLOCKDATA对象块结束的标志.

    0x70:TC_NULL，没有超类了。

    00 00 00 0B: 11, containVersion的值.


'''