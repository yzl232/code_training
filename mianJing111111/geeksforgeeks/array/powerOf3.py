# encoding=utf-8
'''
check一个数是否是3的次幂
if (n == 0) {
   return false;
}

while (n % 3 == 0) {
    n /= 3;
}
return n == 1;

How large is your input? With O(log(N)) memory you can do faster, O(log(log(N)). Precompute the powers of 3 and then do a binary search on the precomputed values.



网上搜了下，一个思路是把这个数的每一位想加用和除以3，再将得数相加，继续除3，直到得数为1，如果在这个过程中没有余数，也就是说可以一直都除尽那么这个数就是3的幂。

还有个思路是 二分查表

查表法。应当会很好。
可以不可以就 int b=3
while(a>b){
b*=3;
}
return a==b

可以简化二分查找，找3^1, 3^2, 3^4, 3^8, 3^16,...知道3^(2^n) 刚好比原来的数num小，然后除，得到的商再依次扫描3^(2^(n-1)), 3^(2^(n-2)),...，哪个比商小就除在得到商，一直到最后看是否能除尽得到1，时间复杂度是log（log（num））

#
一个思路是把这个数的每一位想加用和除以3，再将得数相加，继续除3，直到得数为1，如果在这个过程中没有余数，也就是说可以一直都除尽那么这个数就是3的幂。
非常快。

27， 81， 243
'''


'''
while (n % 3 == 0) {
    n /= 3;
}
return n == 1;
'''