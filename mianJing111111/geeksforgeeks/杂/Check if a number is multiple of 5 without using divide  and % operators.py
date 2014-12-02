# encoding=utf-8
#一直用减法。  或者是转化为string，看最后一位。
'''

Check if a number is multiple of 5 without using / and % operators



Method 1 (Repeatedly subtract 5 from n)
Run a loop and subtract 5 from n in the loop while n is greater than 0. After the loop terminates, check whether n is 0. If n becomes 0 then n is multiple of 5, otherwise not.
#include<stdio.h>

/* assumes that n is a positive integer */
bool isMultipleof5 (int n)
{
    while ( n > 0 )
        n = n - 5;

    if ( n == 0 )
        return true;

    return false;
}

/* Driver program to test above function */
int main()
{
    int n = 19;
    if ( isMultipleof5(n) == true )
        printf("%d is multiple of 5\n", n);
    else
        printf("%d is not a multiple of 5\n", n);

    return 0;
}

Method 2 (Convert to string and check the last character)
Convert n to a string and check the last character of the string. If the last character is ‘5’ or ‘0’ then n is multiple of 5, otherwise not.
'''