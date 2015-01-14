# encoding=utf-8
# Explain what happens, step by step, after you type a URL into a browser. Use as much detail as possible.

# cracking coding interview
'''
1. Browser contacts the DNS server to find the IP address of URL.
2. DNS returns back the IP address of the site.
# 向DNS sever索要url对应的ip, 返回
3. Browser opens TCP connection to the web server at port 80.
4. Browser fetches the html code of the page requested.
#建立tcp连接。  获取html内容。
5. Browser renders the HTML in the display window.
6. Browser terminates the connection when window is closed.
# 关闭窗口，连接结束。

One of the most interesting steps is Step 1 and 2 - “Domain Name Resolution.” The web ad- dresses we type are nothing but an alias to an IP address in human readable form. Mapping of domain names and their associated Internet Protocol (IP) addresses is managed by the Domain Name System (DNS), which is a distributed but hierarchical entity.
Each domain name server is divided into zones. A single server may only be responsible for knowing the host names and IP addresses for a small subset of a zone, but DNS servers can work together to map all domain names to their IP addresses. That means if one domain name server is unable to find the IP addresses of a requested domain then it requests the information from other domain name servers.
'''