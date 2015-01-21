# encoding=utf-8
'''
Write a program to generate all prime numbers from 2 to N for any N value
'''

#O(n**1.5)

class Solution:
    def sieve(self,n):
        noprimes = set(j for i in range(2, int(n**0.5)+1) for j in range(i*i, n+1, i))   #比如2是prime。  2*2却必然不是。  比如3是。
        return [x for x in range(2, 100) if x not in noprimes]

'''
class Solution:
    def primes(self, n):
        return [i for i in range(2, n+1) if self.isprime(i)]

    def isprime(self, n):
        if n==2 or n==3: return True
        if n%2==0:     return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:    return False
        return True
s = Solution()
print s.primes(100)
'''

'''
http://leetcode.com/2010/04/finding-prime-numbers.html
void prime_sieve(int n, bool prime[]) {
  prime[0] = false;
  prime[1] = false;
  int i;
  for (i = 2; i <= n; i++)
    prime[i] = true;

  int limit = sqrt(n);
  for (i = 2; i <= limit; i++) {
    if (prime[i]) {
      for (int j = i * i; j <= n; j += i)
        prime[j] = false;
    }
  }
}
'''