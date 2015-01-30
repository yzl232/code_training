# encoding=utf-8
'''
# cookie 有那些value?

Cookies are data, stored in small text files, on your computer.

cookie is a way to track users.
(log in, log out)
Cookie( just a long number )

When a web server has sent a web page to a browser, the connection is shut down, and the server forgets everything about the user.

Cookies were invented to solve the problem "how to remember information about the user":

    When a user visits a web page, his name can be stored in a cookie.
    Next time the user visits the page, the cookie "remembers" his name.

Cookies are saved in name-value pairs like:
'''



'''
Browsers are expected to support cookies where each cookie has a size of 4KB, at least 50 cookies per domain, and at least 3000 cookies total.[20] It consists of seven components:[6][26]

    (name, value) pair of the cookie (i.e. name=value)
    Expiry of the cookie
    Path the cookie is good for
    Domain the cookie is good for
    Need for a secure connection to use the cookie
    Whether or not the cookie can be accessed through other means than HTTP (i.e., JavaScript)

logonTicket
SLXab3d24ae100bc3a92f032a1540cd9a61
127.0.0.1/
1537
1150331648
30072937
747296240
30072935
*

-------------------------------------------------------------------



每行对应的含义如下：

cookie名称

cookie值

web访问地址（路径）

安全性，1024和1536表示模指数(MODP)群算法的位数

cookie有效日期

修改日期

建立日期

建立者


在jsp中处理cookie数据的常用方法



getComment();返回cookie的注释
getDomain();返回cookie的域名.
getMaxAge();返回cookie的存活时间
getName();返回cookie的名字
getPath();返回cookie适用的路径
getSecure();如果浏览器通过安全协议发送Cookie将返回true值,如果浏览器使用标准协议刚返回false值
getValue();返回cookie的值
getVersion();返回cookie所遵从的协议版本
setComment(String purpose);设置cookie的注释
setDomain(String domain);设置cookie的唯一使用者
setMaxAge(int maxAge);设置cookie的有效期
setPath(String url);设置Cookie的适用路径
setSecure(Boolean flag);设置浏览器是否仅仅使用安全协议来发送cookie，例如使用Https或ssl
setValue(String newvalue);cookie创建后设置一个新的值
setVersion(int v);设置cookie所遵从的协议版本.




'''