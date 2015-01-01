# encoding=utf-8

'''
First, Google has such a service @ //goo.gl/
Second, one URL A is transferred:
one URL B is send to google server and get A;
the browser auto get page using URL A;
Length(B) << Length(A)
So, it is not compress the URL A, but build a URL mapping service.
'''
#G家超高频


#所以google的search suggest, //goo.gl/是一定要研究的

#超高频。看到不下5次。


#http://www.hiredintech.com/app#the-system-design-process

'''
Consider the question about the URL-shortening service ("Design a URL shortening service like bit.ly"). There are so many things that are unclear about it! Without knowing more, it will be impossible to design an appropriate solution. Actually, many candidates forget about this and start designing a solution immediately.

Don’t make this mistake!

The very first thing you should do with any system design question is to clarify the system's constraints and to identify what use cases the system needs to satisfy. Spend a few minutes questioning your interviewer and agreeing on the scope of the system.
'''





'''
For example, the URL-shortening service could be meant to serve just a few thousand users, but each could be sharing millions of URLs. It could be meant to handle millions of clicks on the shortened URLs, or dozens. The service may have to provide extensive statistics about each shortened URL (which will increase your data size), or statistics may not be a requirement at all.

You will also have to think about the use cases that are expected to occur. Your system will be designed based on what it's expected to do. Don't forget to make sure you know all the requirements the interviewer didn't tell you about in the beginning.
'''




'''
While shortening the URL:

Store the Long URL in a DB table which has an auto-generated identity column (increments by 1 each record)

Next write an algorithm to convert the integer ID of this database record in to a base 62 number and then represent the number in base62:
where a-z are mapped to 0-25
A-Z are mapped to 26-51
and 0-9 are mapped to 52-61

essentially we want to say that the shortened URL would contain a-z; A-Z and/or 0-9 characters only

//Check if URL exists in Table; if so fetch that id from DB and process; if not then insert URL in DB and process


String APPLICABLE_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

	public String getShortURLFromID(int dbID){

		List<Integer> digits= new ArrayList<Integer>();
		while (dbID > 0) {
			int  remainder =  dbID % BASE;
			digits.add(remainder);
			dbID= dbID/ BASE;
		}

		Collections.reverse(digits);

		StringBuilder shortCode = new StringBuilder(digits.size());
		for(int i=0; i<digits.size(); i++){
			shortCode.append(APPLICABLE_CHARS.charAt(digits.get(i)));
		}

		return shortCode.toString();
	}

While retrieving the complete URL from Short URL; we need to decode the shortURL to get the DB ID out of it.

Example: if shortened URL was kkDN

k maps to 10 in our APPLICABLE_CHARS String
D maps to 29
and N maps to 39

then DB ID = 10 X 62^ 3 + 10 X 62^2 + 29 X 62 ^1 + 39 X 62 ^0
= 2383280 + 38440 + 1798 + 39
= 2423557

public static int getDbIdFromShortURL(String shortURL) {

		int dbID = 0;

		for(int i=0, j=shortURL.length()-1; i < shortURL.length() && j > -1; i++, j--){
			char letter = shortURL.charAt(i);
			int digit = APPLICABLE_CHARS.indexOf(letter);
			dbID += digit * Math.pow(BASE, j);
		}

		return dbID;

	}
'''

'''
说个hash真不知道是什么意思
首先弄清楚
1. 要不要支持自定义的shorten url
2. 任何人都可以生成shorten url呢还是只有登录的用户才可以
3. 一样的full url要不要给一样的shorten url
然后最基本的
1. shorten url是什么形式，多长，为什么，encode id to base 62?
2. 如何维护shorten url -> full url的mapping，id => full url?
3. 如何生成id? 会不会有collision, 如何解决
再说几点吧
1. 如何防止生成的url被scan，比如我知道某id=abc是合法的，然后试id-1 和id+1 不
应该被猜中
2. 如果要求随机猜N个url都未命中的概率大于99.99%，如何做到
3. 如果有人随机猜url 对你的系统有什么影响，如果你是persistant storage+cache
的架构 会有什么问题
4. 如何distribute到多机器 service和storage 都谈谈
5. 如何要限制单个用户的rps，用什么策略，如何实现

'''
#  二楼的问题问的很好，很多时候不是问题难，而是后面的follow up 看水平。所以有很
#多题觉得会了，真正遇到了follow up才知道理解的不对。

#http://www.quora.com/What-is-the-architecture-of-a-scalable-URL-shortener

'''
这个题常见解法不是hash
直接把URL插入数据库，用DB中index生成tiny URL
'''

'''
db index方法可以解决冲突问题哦 而且还可以保证 这个全局index不断增长，这样就
加个读写lock防止并发访问就行了吧。。
'''

#http://www.quora.com/What-is-the-architecture-of-a-scalable-URL-shortener
#很长的答案

#http://blog.codinghorror.com/url-shortening-hashes-in-practice/
#一篇文章


#http://stackoverflow.com/questions/742013/how-to-code-a-url-shortener



'''
 267 down vote favorite
322


I want to create a URL shortener service where you can write a long URL into an input field and the service shortens the URL to "http://www.example.org/abcdef". Instead of "abcdef" there can be any other string with six characters containing a-z, A-Z and 0-9. That makes 56~57 billion possible strings.

Edit: Due to the ongoing interest in this topic, I've uploaded the code that I used to GitHub, with implementations for Java, PHP and JavaScript. Add your solutions if you like :)

My approach:

I have a database table with three columns:

    id, integer, auto-increment
    long, string, the long URL the user entered
    short, string, the shortened URL (or just the six characters)

I would then insert the long URL into the table. Then I would select the auto-increment value for "id" and build a hash of it. This hash should then be inserted as "short". But what sort of hash should I build? Hash algorithms like MD5 create too long strings. I don't use these algorithms, I think. A self-built algorithm will work, too.


'''